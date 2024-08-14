# IMAGEM PARA ICO
🎈USE ESSE APP PARA REMOVER O FUNDO DAS SUAS FOTOS E CONVERTER PARA ICO (ICONE).

<img src="FOTO.png" align="center" width="500"> <br>

## DESCRIÇÃO:
Este aplicativo é uma interface gráfica simples que permite aos usuários selecionar uma imagem de qualquer formato e remover o fundo da imagem usando a biblioteca `rembg`. Após remover o fundo, a imagem é convertida para o formato de ícone (.ico) usando a biblioteca `PIL` (Python Imaging Library). Finalmente, o aplicativo salva a imagem resultante, agora com o fundo removido e no formato de ícone, no mesmo diretório em que a imagem original foi selecionada.

## FUNCIONALIDADES:
1. **Selecionar Imagem**: Os usuários podem clicar no botão "SELECIONAR" para escolher uma imagem de qualquer formato em seus sistemas de arquivos locais.
  
2. **Remover Fundo e Salvar como Ícone**: Depois de selecionar a imagem, o usuário pode clicar no botão "SALVAR" para iniciar o processo de remoção do fundo e conversão para o formato de ícone (.ico). Uma vez concluído o processo, a imagem resultante é salva no mesmo diretório da imagem original.

3. **Feedback de Sucesso**: Após a conclusão bem-sucedida do processo de remoção de fundo e conversão para ícone, uma caixa de diálogo é exibida informando ao usuário que o fundo foi removido e a imagem foi salva com sucesso.

## EXECUTANDO ESSE PROJETO:
1. **Instalação das Dependências::**
   - Entre no diretório `CODIGO` e execute o comando:

   ```bash
   pip install -r requirements.txt
   ```

2. Para executar o arquivo Python, utilize o comando abaixo no terminal, dentro do diretório `./CODIGO`:

   ```
   python CODIGO.py
   ```

3. Isso abrirá uma janela do aplicativo "IMAGEM PARA ICO".
4. Clique no botão "SELECIONAR" para escolher a imagem da qual deseja criar o ícone.
5. Após selecionar a imagem, clique no botão "SALVAR" para iniciar o processo de remoção do fundo e salvar a imagem como ícone.
6. Aguarde até que o processo seja concluído. Quando terminar, uma mensagem de sucesso será exibida.
7. O ícone com o fundo removido será salvo no mesmo diretório da imagem original, com o sufixo "_ICONE.ico" adicionado ao nome do arquivo.

## POR QUE CRIEI ESTE APLICATIVO?
- Desenvolvi este aplicativo porque me vi frequentemente frustrado por precisar abrir o `GIMP` apenas para converter imagens em ícones depois de remover o fundo delas. Esta solução simplificou significativamente a vida de quem necessita criar ícones para seus aplicativos.

- Na verdade, este projeto é uma extensão do [REMOVEDOR DE FUNDO DE IMAGEM](https://github.com/VILHALVA/REMOVEDOR-DE-FUNDO-DE-IMAGEM). A principal distinção é que este aplicativo converte automaticamente a imagem em um ícone após remover o fundo.
  
## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos disponíveis:
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CURSO DE TKINTER](https://github.com/VILHALVA/CURSO-DE-TKINTER)
* [SAIBA MAIS SOBRE O "REMBR"](https://github.com/danielgatis/rembg)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)

## CREDITOS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)
- [VERSÃO MELHORADA DO "REMOVEDOR DE FUNDO DE IMAGEM"](https://github.com/VILHALVA/REMOVEDOR-DE-FUNDO-DE-IMAGEM)






