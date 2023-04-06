# API tests

Репозиторий включает в себя следующие API тесты:

1) Сайт https://demowebshop.tricentis.com (тесты влючают в себя проверку UI и API)
  - Проверка авторизации пользователя
  - Проверка добавления товара в корзину
  - Проверка добавления товара в избранное
  - Проверка данных пользователя
  - Проверка выхода пользователя из профиля

2) Сайт https://reqres.in (тесты влючают в себя проверку API)
  - Проверка статус кода Ответа метода GET /api/users/1
  - Проверка Ответа метода GET /api/users/1 на наличие поля "first_name"
  - Проверка поля "email" на наличие "@reqres.in" в Ответе метода GET /api/users/1
  - Проверка Ответа метода GET /api/users/1 на соответствие схеме
  - Проверка выхода пользователя из профиля

## <img width="30px" title="Jenkins" src="https://user-images.githubusercontent.com/118905261/230335250-74a96dcc-6029-423c-9faf-f4551b7a9448.png"> Запуск проекта в Jenkins

[Ссылка на сборку](https://jenkins.autotests.cloud/job/alexsakriv_qa_guru_python_3_10/)

При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение, через виртуальную машину в Selenide.

<img width="1728" alt="Снимок экрана 2023-04-06 в 12 40 54" src="https://user-images.githubusercontent.com/118905261/230338674-724129f4-3e2e-4faa-bdb5-bd7156b0ac06.png">

После сборки тестов формируется Allure отчет. Открыть его можно нажав на иконку  <img width="10px" title="Allure Report" src="https://user-images.githubusercontent.com/118905261/230338875-2f21268b-e367-4705-b7a8-a5a9ef1698d2.png">

<img width="1728" alt="Снимок экрана 2023-04-06 в 12 41 10" src="https://user-images.githubusercontent.com/118905261/230338695-2eeb419c-fd23-4f21-ac39-71261fe612f4.png">

## <img width="30px" title="Allure Report" src="https://user-images.githubusercontent.com/118905261/230338875-2f21268b-e367-4705-b7a8-a5a9ef1698d2.png"> Allure отчет

Вкладка "Overview" включает в себя отчет по тесту, дату прохождения теста и затраченное время на прохождение теста

<img width="1728" alt="Снимок экрана 2023-04-06 в 12 45 27" src="https://user-images.githubusercontent.com/118905261/230340031-95d63f15-8c50-460e-92dd-671ea37af2fa.png">

На вкладке "Suites" можно найти подробную информацию о тесте: предусловия, шаги теста и вложения (скриншот, видео и логи)

<img width="1728" alt="Снимок экрана 2023-04-06 в 12 45 45" src="https://user-images.githubusercontent.com/118905261/230340065-bd50f0b7-cc5e-4005-a0c2-4569a4caae51.png">

Видео прохождения теста:

https://jenkins.autotests.cloud/job/alexsakriv_qa_guru_python_3_10/21/allure/data/attachments/dd6bec149e4e10a1.html

## <img width="30px" title="Tg" src="https://user-images.githubusercontent.com/118905261/230376221-fc9f88c7-a18f-4cda-b867-e1bb9abfe0c2.png"> Отчет в Телеграм

В результате выполнения теста отправляется отчет в Телеграм с временем выполнения теста и ссылкой на Allure отчет

<img width="326" alt="Снимок экрана 2023-04-06 в 15 17 41" src="https://user-images.githubusercontent.com/118905261/230376608-0aef9327-c892-4a7a-aba6-13999a28fcc4.png">


