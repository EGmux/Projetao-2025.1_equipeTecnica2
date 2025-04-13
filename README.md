# equipe-api
Membros da equipe responsável por implementar a API do SkateCoach

# Para preparar ambiente de desenvolvimento:

- Tenha instalado uma versão do **Python >= 3.13**

- Execute o seguinte comando que criará um ambiente virtual para não ocorrer conflito de depedências:
    ```bash
    python -m venv equipe-api
    ```
- Execute o seguinte comando para definir o ambiente virtual previamente definido como o utilizado para instalações de depedências

    ```bash
    source equipe-api/bin/activate
    ```
- Execute o seguinte comando para instalar as depedências do projeto 
    
    ```bash
    pip install -r requirements.txt
    ```

*Ao realizar uma operação de pull considere executar tal comando para manter as depedências atualizadas no seu ambiente virtual*

*Caso modifique alguma depedência do projeto ou adicione uma execute o seguinte comando para manter o arquivo requirements.txt atualizado*

```bash
rm requirements.txt ; pip freeze > requirements.txt
```

# Para testar o módulo

## Testes unitários

👷‍ **EM CONSTRUÇÃO**

# Estrutura do projeto

````
./requirements.txt      # definição das depedências
./module               
   ├── __init__.py      # identifica diretório como pacote python
   ├── main.py          # ponto de entrada do módulo
   ├── dependencies.py  # depedências do projeto importadas aqui
   ├── test_data  # artefatos para testes
                ./output.csv            # artefato para testes
   ├── components  
   │             ├── __init__.py  
   │             ├── action.py
   │             ├── movement.py
   │             ├── coach.py
   │             ├── utils.py
   │             ├── test_action.py 
   │             ├── test_movement.py 
   │             ├── test_coach.py 
````

# Contribuir para este repositório

- Fork esse repositório

- Crie ou dê checkout numa das branch com o nome do componente que deseja trabalhar ou main caso deseje modificar arquivos que não fazem parte de um componente, tais como main.py, depedencies.py ou requirements.txt

- submita um pull request
