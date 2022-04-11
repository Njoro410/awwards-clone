
# Awwards-clone

An awwards clone where users can post projects and have them rated and reviewed by other users
## Live Link


https://awwards5652.herokuapp.com/
## Authors

- [Brian Njoroge](https://github.com/Njoro410)


## Features

- Create account
- View projects
- Add projects
- Rate and review projects



## Deployment

This project has been deployed to Heroku


## Run Locally

Clone the project

```bash
https://github.com/Njoro410/awwards-clone.git
```

Go to the project directory

```bash
  cd awwards-clone
```

Install dependencies

```bash
  pip install -r requirements.txt
```


Start the server

```bash
  python3 manage.py runserver
```


## Tech Stack

- [Python 3.8.10](https://www.python.org/)
- [Django v.4](https://docs.djangoproject.com/en/4.0/releases/4.0/)
- [Django-Material](https://getbootstrap.com/)



## Running Tests

To run tests, run the following command

```
python3 manage.py test
```

## License

- [MIT](https://choosealicense.com/licenses/mit/)
- [Apache License 2.0](https://opensource.org/licenses/Apache-2.0)


## Feedback

If you have any feedback, please reach out to me at briannjoroge420@gmail.com


## API Reference

### Source
```
https://awwards5652.herokuapp.com/api/{'endpoints'}
```
#### Get allprojects

```http
  GET https://awwards5652.herokuapp.com/api/allprojects/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id`,`api_key` | `string` | **Required**. Id of item to fetch and API Key |

#### Get project by id

```http
  GET https://awwards5652.herokuapp.com/api/specificProject/{}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Get user's details

```http
  GET https://awwards5652.herokuapp.com/api/userDetails/{}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Get user's Projects

```http
  GET https://awwards5652.herokuapp.com/api/userProjects/{}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


#### Get user's profile details
```http
  GET https://awwards5652.herokuapp.com/api/profile/{}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |




