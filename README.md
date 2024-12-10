# Cico Tunnel  

O **Cico Tunnel** é uma ferramenta que utiliza SSH para expor portas locais para a internet de forma segura e fácil. Com o Cico Tunnel, você pode criar um túnel SSH para acessar seu servidor local a partir de qualquer lugar.  

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
   pip install cico-tunnel
   ```

## Uso  

Para usar o Cico Tunnel, siga estas etapas:  

1. **Execute o comando `cicotunnel`, passando a porta local que deseja expor**:  

   ```bash
   cicotunnel 80
   ```  

   Isso irá iniciar o Cico Tunnel e criar um túnel para a porta 80 do seu localhost.  
   Se você quiser usar um servidor SSH diferente do padrão, use a flag `-r` ou `--remote` seguido do endereço do seu servidor. Por exemplo:  

   ```bash
   cicotunnel 80 -r usuario@meu.servidor.com
   ```  

2. **Visualize a URL**:  
   O Cico Tunnel exibirá a URL pública para o seu servidor local através do túnel SSH no terminal. Use essa URL para acessar seu servidor local de qualquer lugar na internet.  

## Exemplos  

* Expor a porta do MySQL do localhost no Cico Tunnel:  

  ```bash
  cicotunnel 3306
  ```  

* Expor a porta do MySQL do localhost utilizando um servidor SSH específico:  

  ```bash
  cicotunnel 3306 -r usuario@meu.servidor.com
  ```  

## Contribuindo  

Sinta-se à vontade para contribuir com o projeto! Você pode fazer isso de várias maneiras:  

- **Dar Estrelas**: Se você gostou do Cico Tunnel e acha que ele é útil, considere dar uma estrela ⭐ no [repositório](https://github.com/cicodevada/cico-tunnel). Isso ajuda a apoiar o projeto e mostra que você aprecia o trabalho!  

- **Relatar Problemas**: Se você encontrar algum problema ou bug, por favor, abra uma [issue](https://github.com/cicodevada/cico-tunnel/issues) no repositório.  

- **Enviar Pull Requests**: Se você tem melhorias ou correções, envie um pull request para o repositório.  

- **Feedback**: Qualquer feedback é bem-vindo para ajudar a melhorar o Cico Tunnel.  

---

# Cico Tunnel  

The **Cico Tunnel** is a tool that uses SSH to expose local ports to the internet securely and easily. With Cico Tunnel, you can create an SSH tunnel to access your local server from anywhere.  

## Prerequisites  

Before starting, ensure that you have:  

1. **SSH Access**: You need an SSH server that you can access and have permission to create tunnels.  
   * You can use your own server, but you will need to:  
      - Create an SSH user.  
      - Enable passwordless login.  
      - Allow forwarding and gateway.  
   * Alternatively, you can use the server provided by Cico Tunnel for quick access.  

2. **Python**: Make sure Python is installed on your system. You can download the latest version from [python.org](https://www.python.org/).  

3. **Internet Access**: Required to create the SSH tunnel and access the server.  

## Installation  

1. **Install via pip**:  

   ```bash
   pip install cico-tunnel
   ```

## Usage  

To use Cico Tunnel, follow these steps:  

1. **Run the `cicotunnel` command, specifying the local port you want to expose**:  

   ```bash
   cicotunnel 80
   ```  

   This will start the Cico Tunnel and create a tunnel for port 80 on your localhost.  
   If you want to use a different SSH server, use the `-r` or `--remote` flag followed by your server's address. For example:  

   ```bash
   cicotunnel 80 -r user@my.server.com
   ```  

2. **View the URL**:  
   Cico Tunnel will display the public URL for your local server through the SSH tunnel in the terminal. Use this URL to access your local server from anywhere on the internet.  

## Examples  

* Expose MySQL port from localhost using Cico Tunnel:  

  ```bash
  cicotunnel 3306
  ```  

* Expose MySQL port from localhost using a specific SSH server:  

  ```bash
  cicotunnel 3306 -r user@my.server.com
  ```  

## Contributing  

Feel free to contribute to the project! You can do so in several ways:  

- **Star the Project**: If you like Cico Tunnel and find it useful, consider giving it a ⭐ on the [repository](https://github.com/cicodevada/cico-tunnel). This helps support the project and shows appreciation for the work!  

- **Report Issues**: If you encounter any problems or bugs, please open an [issue](https://github.com/cicodevada/cico-tunnel/issues) on the repository.  

- **Submit Pull Requests**: If you have improvements or fixes, submit a pull request to the repository.  

- **Feedback**: Any feedback is welcome to help improve Cico Tunnel.  
