## Convertendo o Código Python para uma Aplicação Web: Detalhando os Arquivos

**Excelente pergunta!** Vamos decompor a aplicação em seus arquivos individuais e explicar cada um detalhadamente. Lembre-se que esta é apenas uma das muitas formas de estruturar a aplicação, e você pode adaptá-la de acordo com suas necessidades e preferências.

### Estrutura Básica do Projeto

```
plano_inclinado/
├── app.py
├── templates/
│   ├── index.html
│   └── resultado.html
├── static/
│   └── style.css
```

### Explicação de Cada Arquivo

#### `app.py` (Arquivo principal da aplicação Flask)

```python
from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_forcas(massa, angulo, coeficiente_atrito=0):
    # ... (mesmo código Python que você já tem)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # ... (processamento dos dados do formulário)
        return render_template('resultado.html', forcas=forcas)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

* **Importações:** Importa as classes e funções necessárias do Flask para criar a aplicação web.
* **Criação da aplicação:** Cria uma instância da classe Flask, que representa a aplicação web.
* **Função `calcular_forcas`:** A mesma função que você já tinha para calcular as forças.
* **Rota `@app.route('/')`:** Define a rota principal da aplicação.
* **Método HTTP:**
    * `GET`: Exibe o formulário inicial.
    * `POST`: Processa os dados enviados pelo formulário.
* **Renderização de templates:** Utiliza a função `render_template` para renderizar os templates HTML.

#### `templates/index.html` (Formulário de entrada)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Cálculo de Plano Inclinado</title>
    <link rel="stylesheet" href="../static/style.css">
</head>
<body>
    <form method="post">
        </form>
</body>
</html>
```

* **Estrutura HTML:** Define a estrutura básica da página.
* **Link para CSS:** Conecta o arquivo CSS para estilizar a página.
* **Formulário:** Contém os campos para o usuário inserir os dados.

#### `templates/resultado.html` (Página com os resultados)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Resultado</title>
    <link rel="stylesheet" href="../static/style.css">
</head>
<body>
    </body>
</html>
```

* **Estrutura HTML:** Define a estrutura básica da página.
* **Link para CSS:** Conecta o arquivo CSS para estilizar a página.
* **Conteúdo:** Exibe os resultados dos cálculos, utilizando as variáveis passadas do Python.

#### `static/style.css` (Arquivo de estilo)

```css
/* Estilos CSS para a aplicação */
body {
    font-family: Arial, sans-serif;
}
/* ... outros estilos */
```

* **Estilos CSS:** Define os estilos para a página, como fontes, cores, layout, etc.

### Como Rodar a Aplicação

1. **Salvar os arquivos:** Salve os arquivos na estrutura de diretórios indicada.
2. **Instalar Flask:** Se você ainda não tiver instalado, use o comando `pip install Flask` no seu terminal.
3. **Executar o aplicativo:** Execute o arquivo `app.py` no seu terminal.
4. **Acessar a aplicação:** Abra um navegador e digite o endereço indicado no terminal (por exemplo, `http://127.0.0.1:5000/`).

**Observações:**

* **Templates:** O Flask utiliza a biblioteca Jinja2 para renderizar templates. Você pode usar expressões dentro dos templates para exibir dados dinâmicos.
* **Static files:** A pasta `static` é usada para armazenar arquivos estáticos como CSS, JavaScript e imagens.
* **Formulários:** O Flask facilita a criação e o processamento de formulários HTML.
* **Depuração:** O modo de depuração do Flask (`debug=True`) é útil para encontrar e corrigir erros durante o desenvolvimento.

**Personalizações:**

* **Bootstrap:** Utilize o framework Bootstrap para criar layouts responsivos e estilos pré-definidos.
* **JavaScript:** Adicione interatividade à sua aplicação usando JavaScript.
* **Banco de dados:** Para armazenar dados de forma persistente, utilize um banco de dados como SQLite ou PostgreSQL.

**Este é apenas um ponto de partida.** Você pode personalizar e expandir esta aplicação de acordo com suas necessidades, adicionando mais funcionalidades e complexidade.

**Gostaria de ver um exemplo mais completo com Bootstrap e JavaScript?**
