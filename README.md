# Tradutor de Libras

Um projeto desenvolvido por Caio Emmanuel, Letícia Coêlho e Lídia Alves para a disciplina de Visão Computacional.

## How to run

Primeiro, você vai precisar ter [Python](https://www.python.org/) instalado na sua máquina.

Crie e ative um ambiente virtual

```
$ python -m venv env
$ source env/bin/activate
```

O comando para ativar pode ser diferente se você usar algum sistema operacional esquisito (como o Windows).

Instale poetry e em seguida instale as dependências

```
$ pip install poetry
$ poetry install
```

Execute a aplicação

```
$ python main.py
```

Para rodar a coleta de dados

```
$ python utils/data_collection.py
```

## Demonstração

- [Demonstrativo aplicação](https://drive.google.com/file/d/13m20RhY6cd3sjp3o8TEN5yJPG7a76bKo/view?usp=sharing)
- [Demonstrativo coleta de dados](https://drive.google.com/file/d/16gEJx_UWCS1SQQlF9RlcUcRIC3OZJqkM/view?usp=sharing)

## Deploy

Para fazer deploy você irá precisar instalar o aplicativo [Deta Space](https://deta.space/docs/en/build/fundamentals/space-cli).

Você pode seguir [esse tutorial](https://deta.space/docs/en/build/quick-starts/python/) ou simplesmente executer

`$ space push`

## Referências

- [MediaPipe](https://developers.google.com/mediapipe)
- [Tensorflow](https://www.tensorflow.org/?hl=pt-br)
- [Adicionar novos sinais de mão](https://github.com/kinivi/hand-gesture-recognition-mediapipe)
- [Deta Space](https://deta.space/docs/en/build/quick-starts/python/)