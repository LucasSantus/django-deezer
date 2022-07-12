<h1 align="center">Deezer</h1>

<h6 align="center"> 
	Se você quiser visualizar o sistema, clique <a href="https://github.com/LucasSantus/django-deezer">aqui</a>.
</h6>

<h3 id="sobre">:information_source: Sobre</h3>

> Este projeto foi desenvolvido utilizando o Django Framework como back-end e Bootstrap 5 no front-end. 

A ideia é:

_"Criar um projeto consumindo a API do Deezer(PLayer de Música). Tendo como objetivo a construção do backend da aplicação com intuito de promover o aprendizado na área relacionado ao Django Framework."_

--------------------------------------------------------------------------------------

<h3 id="tabela-de-conteudo">:ab: Tabela de Conteúdo</h3>

* [Sobre](#sobre)
* [Tabela de Conteudo](#tabela-de-conteudo)
* [Status do Projeto](#status)
* [Por Que](#por-que)
* [Tecnologias](#tecnologias)
* [Funcionalidades](#funcionalidades)
* [Instalação do Projeto](#instalando)
    * [Clonando Repositório](#clonando)
    * [Windows](#rodando-windows)
    * [Linux](#rodando-linux)
* [Autor](#autor)
* [Licença](#license)

--------------------------------------------------------------------------------------

<h3 id="status">:heavy_exclamation_mark: Status do Projeto</h3>

<h4 align="center">
 :construction: Sistema Web em andamento... :construction:
</h4>

--------------------------------------------------------------------------------------

<h3 id="por-que">:question: Por Que</h3>

Este projeto faz parte do meu portfólio pessoal, ficarei feliz caso você forneça algum feedback, código, estrutura, funcionalidade ou qualquer funcionalidade&melhoria que você possa relatar para melhora-lo.

Você pode usar este projeto como quiser, seja para estudar, fazer melhorias, você que manda!

Este é um projeto totalmente grátis!

--------------------------------------------------------------------------------------

<h3 id="tecnologias">:rocket: Tecnologias</h3>

As seguintes ferramentas foram usadas na construção do projeto:

- [Django Framework 3.2](https://www.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Django Form Bootstrap V5](https://pypi.org/project/django-bootstrap-v5/)
- [Django Debug Toolbar 3.2.4](https://pypi.org/project/django-debug-toolbar/3.2.4/)

--------------------------------------------------------------------------------------

<h3 id="funcionalidades">:sparkles: Funcionalidades</h3>

- [X] Possibilita ...

--------------------------------------------------------------------------------------

<h3 id="instalando">:computer: Instalando o Projeto</h3>

<h4 id="clonando">Clonando o Repositório</h4>

```
git clone git@github.com:LucasSantus/django-deezer.git

cd django-deezer
```

<h4 id="rodando">Rodando o Projeto</h4>

> Antes de rodar o projeto, é necessário configurar o settings_local.py

<h4 id="rodando-windows">
	<strong>Windows</strong>
</h4>

> **Observação:** Foi utilizado o Windows(versão 10), caso ocorra algum problema na instalação, pesquise por conta própria a resolução do mesmo!

```
python -m venv env

env\Scripts\activate

python -m pip install --upgrade pip

pip install -r requirements.txt

python manage.py makemigrations home

python manage.py makemigrations deezer

python manage.py migrate

python manage.py runserver
```

<h4 id="rodando-linux">
	<strong>Linux</strong>
</h4>

> **Observação:** Foi utilizado a distro Linux Mint(versão 20.1), caso ocorra algum problema na instalação, pesquise por conta própria a resolução do mesmo!

**Preparando Ambiente Virtual**

Com o terminal aberto, digite no terminal:

```
python3 -m venv env

source env/bin/activate

python -m pip install --upgrade pip

pip install -r requirements.txt

python manage.py makemigrations home

python manage.py makemigrations deezer

python manage.py migrate

python manage.py runserver
```

**Criando Super Usuário**

```
python manage.py createsuperuser
```

**Acessando o Projeto**

para visualizar o projeto: http://127.0.0.1:8000/

**Acessando o Admin**

Com o projeto rodando, adicione o 'admin/' dps da URL:

http://127.0.0.1:8000/admin/

--------------------------------------------------------------------------------------

<h3 id="autor">:bust_in_silhouette: Autor</h3>

<table>
	<tr>
		<td>
			<div> 
				<a href="https://github.com/LucasSantus">
					<img style="border-radius: 50%;" src="https://github.com/LucasSantus.png" width="100px;" alt=""/>
					<br />
					Lucas Santus
				</a>
			</div>
		</td>
	</tr>
</table>
<br />
Feito com ❤️ por Lucas Santus!<br />
Obrigado por visitar e boa codificação!<br />

--------------------------------------------------------------------------------------

<h3 id="license">:memo: License</h3>

Este projeto está licenciado sob a Licença MIT License - veja o [LICENSE.md](https://github.com/LucasSantus/django-deezer/blob/master/LICENSE) para melhores detalhes.

