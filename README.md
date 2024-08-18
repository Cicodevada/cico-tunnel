# Cico Tunnel

O **Cicotunnel** é uma ferramenta que utiliza SSH para expor portas locais para a internet de forma segura e fácil. Com o Cico Tunnel, você pode criar um túnel SSH para acessar seu servidor local a partir de qualquer lugar.

## Pré-requisitos

Antes de começar, certifique-se de que você possui:

1. **Acesso SSH**: Você precisa de um servidor SSH ao qual você tenha acesso e permissão para criar túneis. (Pode usar o meu proprio servidor também caso queira algo rapido)

1.1 **Caso queira usar o seu próprio servidor**, você precisa:
   - Criar um usuário SSH.
   - Permitir login sem senha.
   - Permitir o forwarding e o gateway.
   
2. **Python**: Certifique-se de que o Python está instalado no seu sistema. Você pode baixar a versão mais recente do Python em [python.org](https://www.python.org/).

3. **Colorama**: Uma biblioteca Python para cores no terminal. É necessária para a interface colorida do Cico Tunnel.

4. **Acesso à Internet**: É necessário para criar o túnel SSH e acessar o servidor.

## Instalação

1. **Clone o Repositório**:
   Primeiro, clone o repositório do Cico Tunnel para o seu sistema:
   ```sh
   git clone https://github.com/hugosantoslisboa/cico-tunnel.git
   cd cico-tunnel
   ```
   
2. **Instale as Dependências**:
   Instale o Colorama usando pip:
   ```pip install colorama```

## Uso

Para usar o Cico Tunnel, siga estas etapas:

1. **Clone o Repositório**:
   Execute o script principal, passando a porta local que deseja expor e a configuração SSH como argumentos:
   ```py main.py PORTA
   Exemplo: py main.py 80
   ```
   
2. **Visualize a URL**:
   O Cico Tunnel exibirá a URL pública para o seu servidor local através do túnel SSH no terminal. Use essa URL para acessar seu servidor local de qualquer lugar na internet.



## Contribuindo

Sinta-se à vontade para contribuir com o projeto! Você pode fazer isso de várias maneiras:

- **Dar Estrelas**: Se você gostou do Cicotunnel e acha que ele é útil, considere dar uma estrela ⭐ no [repositório](https://github.com/hugosantoslisboa/cico-tunnel). Isso ajuda a apoiar o projeto e mostra que você aprecia o trabalho!

- **Relatar Problemas**: Se você encontrar algum problema ou bug, por favor, abra uma [issue](https://github.com/hugosantoslisboa/cico-tunnel/issues) no repositório.

- **Enviar Pull Requests**: Se você tem melhorias ou correções, envie um pull request para o repositório.

- **Feedback**: Qualquer feedback é bem-vindo para ajudar a melhorar o Cico Tunnel.
