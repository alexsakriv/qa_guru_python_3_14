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
  - Проверка статус кода Ответа метода POST /api/users
  - Проверка Ответа метода POST /api/users на наличие поля "name"
  - Проверка Ответа метода POST /api/users на соответствие схеме
  - Регистрация пользователя с помощью метода POST /api/register и проверка авторизации зарегистированного пользователя

## <img width="30px" title="Jenkins" src="https://user-images.githubusercontent.com/118905261/230335250-74a96dcc-6029-423c-9faf-f4551b7a9448.png"> Запуск проекта в Jenkins

[Ссылка на сборку](https://jenkins.autotests.cloud/job/api_tests_alexsakriv/)

При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение, через виртуальную машину в Selenide.

<img width="1728" alt="Снимок экрана 2023-04-06 в 12 40 54" src="https://user-images.githubusercontent.com/118905261/230443236-2a4e02af-59d7-4624-bd49-f012017c4086.png">

После сборки тестов формируется Allure отчет. Открыть его можно нажав на иконку  <img width="10px" title="Allure Report" src="https://user-images.githubusercontent.com/118905261/230338875-2f21268b-e367-4705-b7a8-a5a9ef1698d2.png">

<img width="1728" alt="Снимок экрана 2023-04-06 в 12 41 10" src="https://user-images.githubusercontent.com/118905261/230443270-e528cd91-7d89-4914-973e-466c63ec58dc.png">

## <img width="30px" title="Allure Report" src="https://user-images.githubusercontent.com/118905261/230338875-2f21268b-e367-4705-b7a8-a5a9ef1698d2.png"> Allure отчет

Вкладка "Overview" включает в себя отчет по тесту, дату прохождения теста и затраченное время на прохождение теста

<img width="1728" alt="Снимок экрана 2023-04-06 в 12 45 27" src="https://user-images.githubusercontent.com/118905261/230443589-1baf42ab-34a3-4449-97ac-cb1629203880.png">

На вкладке "Suites" можно найти подробную информацию о тесте: предусловия, шаги теста и вложения (скриншот, видео и логи)

<img width="1728" alt="Снимок экрана 2023-04-06 в 12 45 45" src="https://user-images.githubusercontent.com/118905261/230443865-3a48c6cd-f54b-4afc-81f2-f9a883b7053d.png">

Видео прохождения теста Добавления товара в корзину "test_add_product_to_cart":

https://jenkins.autotests.cloud/job/api_tests_alexsakriv/4/allure/data/attachments/905e6d5cc7cc783f.html


