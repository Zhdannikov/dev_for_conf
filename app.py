from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
from datetime import datetime
import os 
# CHANGEEEE FOR 5 LAB TO START CICD
# NEW PR
app = Flask(__name__)


MONGO_URI = os.getenv('MONGO_URI', 'mongodb://admin:secret@mongo:27017/myapp?authSource=admin')
client = MongoClient(MONGO_URI)
db = client.conference_db
participants = db["participants"]  # коллекция участников

# Главная страница
@app.route("/")
def index():
    return render_template("index.html")


# 1) Список приглашённых по дате 1-го приглашения
@app.route("/invited_by_first_mail", methods=["GET", "POST"])
def invited_by_first_mail():
    if request.method == "POST":
        date_str = request.form.get("date")
        try:
            target_date = datetime.strptime(date_str, "%Y-%m-%d")
            # Ищем по дате без времени
            invited = list(participants.find({
                "conference.first_invitation_date": {
                    "$gte": target_date,
                    "$lt": datetime(target_date.year, target_date.month, target_date.day, 23, 59, 59)
                }
            }))
            count = len(invited)
        except ValueError:
            invited = []
            count = 0
        return render_template("invited_list.html", participants=invited, count=count, date=date_str)
    return render_template("invited_by_first_mail.html")


# 2) Добавление нового участника
@app.route("/add_participant", methods=["GET", "POST"])
def add_participant():
    if request.method == "POST":
        # Персональные данные
        personal = {
            "last_name": request.form.get("last_name"),
            "first_name": request.form.get("first_name"),
            "patronymic": request.form.get("patronymic"),
            "academic_degree": request.form.get("academic_degree"),
            "academic_title": request.form.get("academic_title"),
            "scientific_field": request.form.get("scientific_field"),
            "workplace": request.form.get("workplace"),
            "department": request.form.get("department"),
            "position": request.form.get("position"),
            "country": request.form.get("country"),
            "city": request.form.get("city"),
            "postal_code": request.form.get("postal_code"),
            "address": request.form.get("address"),
            "work_phone": request.form.get("work_phone"),
            "home_phone": request.form.get("home_phone"),
            "email": request.form.get("email"),
        }

        # Информация о конференции
        conference_info = {
            "role": request.form.get("role"),  # докладчик / участник
            "first_invitation_date": parse_date(request.form.get("first_invitation_date")),
            "application_date": parse_date(request.form.get("application_date")),
            "presentation_title": request.form.get("presentation_title"),
            "thesis_received": bool(request.form.get("thesis_received")),
            "second_invitation_date": parse_date(request.form.get("second_invitation_date")),
            "payment_date": parse_date(request.form.get("payment_date")),
            "payment_amount": float(request.form.get("payment_amount") or 0),
            "arrival_date": parse_date(request.form.get("arrival_date")),
            "departure_date": parse_date(request.form.get("departure_date")),
            "needs_hotel": bool(request.form.get("needs_hotel")),
        }

        # Сохраняем в БД
        participants.insert_one({
            "personal": personal,
            "conference": conference_info,
            "created_at": datetime.now()
        })

        return redirect(url_for("index"))

    return render_template("add_participant.html")


# 3) Список приглашённых с датой уплаты оргвзноса
@app.route("/payments_list")
def payments_list():
    # Все, кто уплатил оргвзнос (payment_amount > 0)
    paid = list(participants.find({
        "conference.payment_amount": {"$gt": 0}
    }))
    return render_template("payments_list.html", participants=paid)


# 4) Участники, уплатившие оргвзнос в заданном диапазоне дат
@app.route("/payments_by_date", methods=["GET", "POST"])
def payments_by_date():
    if request.method == "POST":
        start_str = request.form.get("start_date")
        end_str = request.form.get("end_date")
        try:
            start = datetime.strptime(start_str, "%Y-%m-%d")
            end = datetime.strptime(end_str, "%Y-%m-%d")
            # Включаем весь день окончания
            end = end.replace(hour=23, minute=59, second=59)

            result = list(participants.find({
                "conference.payment_date": {"$gte": start, "$lte": end},
                "conference.payment_amount": {"$gt": 0}
            }))
        except ValueError:
            result = []
        return render_template("payments_by_date.html", participants=result, start=start_str, end=end_str)
    return render_template("payments_by_date_form.html")


# 5) Названия тезисов по городу
@app.route("/thesis_by_city", methods=["GET", "POST"])
def thesis_by_city():
    if request.method == "POST":
        city = request.form.get("city")
        thesis_list = list(participants.find({
            "personal.city": city,
            "conference.thesis_received": True
        }, {"conference.presentation_title": 1, "personal.last_name": 1, "personal.first_name": 1}))
        return render_template("thesis_by_city.html", theses=thesis_list, city=city)
    return render_template("thesis_by_city_form.html")


# 6) Список нуждающихся в гостинице по городу
@app.route("/hotel_needed", methods=["GET", "POST"])
def hotel_needed():
    if request.method == "POST":
        city = request.form.get("city")
        hotel_list = list(participants.find({
            "personal.city": city,
            "conference.needs_hotel": True
        }))
        return render_template("hotel_needed.html", participants=hotel_list, city=city)
    return render_template("hotel_needed_form.html")


# Вспомогательная функция для парсинга дат
def parse_date(date_str):
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None


if __name__ == "__main__":
    app.run(debug=False)
