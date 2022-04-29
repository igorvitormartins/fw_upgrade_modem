# fw_upgrade_modem

## Código Python desenvolvido com a intenção de automatizar firmware de modems domésticos

### Para o funcionamento deste código, o Dev precisa instalar a biblioteca sellenium e pygame
#####Checar a versão de seu PIP
```terminal

pip.exe install selenium

pip install pygame
```

### Também deve ser feito o download do driver do seu navegador de acordo com a versão

[Chrome WebDriver] (https://www.selenium.dev/documentation/webdriver/)

##### No arquivo config.ini contém campo para informar ip, deve-ser editado de acordo com as informações de acesso de seu modem
##### Este programa foi desenvolvido com uma senha padrão "system" e usuário: "system", e toda tentativa de login era necessário informar um captcha.
O código do programa poderá ser alterado conforme a necessidade, por exemplo, muitos modems não precisam de captcha ao tentar realizar login.

###### Links relacionados:
[Sellenium](https://selenium-python.readthedocs.io/installation.html)
[pygame](https://www.pygame.org/docs/)
