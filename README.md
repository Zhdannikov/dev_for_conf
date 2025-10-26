### **Безопасность**
- **Bandit** - поиск уязвимостей в коде
- **Trufflehog** - поиск секретов в истории гит
- **KubeLinter** - проверка безопасности манифестов

### **Качество кода**  
- **Flake8** - проверка стиля и качества Python кода
- **Hadolint** - анализ Dockerfile на best practices


```bash
# локально
flake8 .                          # качество кода
bandit -r .                       # безопасность питона
docker run --rm -i hadolint/hadolint < Dockerfile  # анализ докерфайла
kube-linter lint kubernetes/      # проверка деплойментов
docker run --rm -v "$(pwd):/workdir" trufflesecurity/trufflehog:latest git file:///workdir --only-verified  # поиск секретов
```
