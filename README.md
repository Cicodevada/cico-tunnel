# Cico Tunnel

O **Cicotunnel** é uma ferramenta que utiliza SSH para expor portas locais para a internet de forma segura e fácil. Com o Cico Tunnel, você pode criar um túnel SSH para acessar seu servidor local a partir de qualquer lugar.

## Pré-requisitos

Antes de começar, certifique-se de que você possui:

1. **Acesso SSH**: Você precisa de um servidor SSH ao qual você tenha acesso e permissão para criar túneis. 
   * Você pode usar seu próprio servidor, mas precisará:
      - Criar um usuário SSH.
      - Permitir login sem senha.
      - Permitir o forwarding e o gateway.
   * Ou você pode usar o servidor fornecido pelo Cico Tunnel para um acesso rápido.
   
2. **Python**: Certifique-se de que o Python está instalado no seu sistema. Você pode baixar a versão mais recente do Python em [python.org](https://www.python.org/).

3. **Acesso à Internet**: É necessário para criar o túnel SSH e acessar o servidor.

## Instalação

1. **Instale via pip**:

   ```bash
   pip install cico-tunnel```

## Uso

Para usar o Cico Tunnel, siga estas etapas:

Execute o comando cicotunnel, passando a porta local que deseja expor:
   ```bash
   cicotunnel 80
   ```
   Isso irá iniciar o Cico Tunnel e criar um túnel para a porta 80 do seu localhost.
2. **Visualize a URL**:
   O Cico Tunnel exibirá a URL pública para o seu servidor local através do túnel SSH no terminal. Use essa URL para acessar seu servidor local de qualquer lugar na internet.



## Contribuindo

Sinta-se à vontade para contribuir com o projeto! Você pode fazer isso de várias maneiras:

- **Dar Estrelas**: Se você gostou do Cicotunnel e acha que ele é útil, considere dar uma estrela ⭐ no [repositório](https://github.com/hugosantoslisboa/cico-tunnel). Isso ajuda a apoiar o projeto e mostra que você aprecia o trabalho!

- **Relatar Problemas**: Se você encontrar algum problema ou bug, por favor, abra uma [issue](https://github.com/hugosantoslisboa/cico-tunnel/issues) no repositório.

- **Enviar Pull Requests**: Se você tem melhorias ou correções, envie um pull request para o repositório.

- **Feedback**: Qualquer feedback é bem-vindo para ajudar a melhorar o Cico Tunnel.
