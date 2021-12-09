<h1 align="center">
    🔗 Exercicio API Denox
</h1>
<p align="center">
  Foi desenvolvido um projeto utilizando 
    <a href="https://www.djangoproject.com/">Django</a>
  e 
    <a href="https://www.python.org/">Python</a> 
  para construição de uma API para calcular distancia de um determinado veiculo.
</p>



### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python](https://www.python.org/), [Virtualenv](https://virtualenv.pypa.io/en/latest/). 
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/).

### 🎲 Rodando o Back End (Projeto)

```bash
# Clone este repositório
$ git clone https://github.com/michel110299/api_desafio

# Acesse a pasta do projeto no terminal/cmd
$ cd api_desafio

# Crie uma nova máquina virtual
$ python -m venv env

#Ative sua máquina virtual(windows)
$env\Scripts\activate

#Ative sua máquina virtual(linux)
$ source env/bin/activate

#Atualize o pip
$ python -m pip install --upgrade pip

#Instale as dependência necessárias do projeto
$ pip install -r requirements.txt

#Rode os seguintes comandos para configurar o projeto
$ python manage.py makemigrations api
$ python manage.py migrate

#Abra o shell do django
$ python manage.py shell

#execute o seguinte comando
$ exec(open('scripts/cadastrarDados.py').read())

#Saia o shell do django
$ exit()

#Para rodar o projeto
python manage.py runserver

```


### Autor
---

<a href="https://github.com/michel110299">
 <img style="border-radius: 50%;" src="https://github.com/michel110299.png" width="100px;" alt=""/>
 <br />
 <sub><b>Michel Lemes </b></sub></a> <a href="https://https://github.com/michel110299" title="Git">:kissing_smiling_eyes:</a>

