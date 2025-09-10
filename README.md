# Discord Bot - Sistema de Assinaturas com Stripe

## Descrição

Este é um bot Discord integrado com Stripe que permite aos usuários comprarem planos de assinatura diretamente através de comandos slash no Discord. O sistema processa pagamentos automaticamente e atribui cargos (roles) aos usuários baseado no plano adquirido.

## Recursos e Funcionalidades

- **Comandos Slash Discord**: Interface intuitiva para compra de planos
- **Integração com Stripe**: Processamento seguro de pagamentos e assinaturas
- **Atribuição Automática de Cargos**: Usuários recebem roles automaticamente após pagamento
- **Webhook Stripe**: Processamento em tempo real de eventos de pagamento
- **Banco de Dados SQLite**: Armazenamento de informações de assinaturas
- **API REST**: Endpoints para webhooks e monitoramento
- **Sistema de Logs**: Rastreamento completo de transações e eventos
- **Planos Configuráveis**: Suporte a múltiplos planos (Premium, VIP, Pro)

### Comandos Disponíveis

- "/comprar plano [nome_do_plano]" - Inicia o processo de compra de um plano

### Eventos Suportados

- **checkout.session.completed** - Atribuição automática de cargo após pagamento
- **customer.subscription.deleted** - Remoção de cargo quando assinatura é cancelada

## Tecnologias Utilizadas

- **.NET 9.0** - Framework principal
- **ASP.NET Core** - Web API para webhooks
- **Discord.Net 3.18.0** - Biblioteca para integração com Discord
- **Stripe.NET 48.5.0** - SDK oficial do Stripe para .NET
- **Entity Framework Core 9.0.8** - ORM para banco de dados
- **SQLite** - Banco de dados local
- **Swagger/OpenAPI** - Documentação da API

## Instruções

### 1. Pré-requisitos

- **.NET 9.0 SDK** instalado
- **Conta Discord Developer** e bot criado
- **Conta Stripe** com API keys
- **Git** para controle de versão

#### Links úteis:
- [Download .NET 9.0](https://dotnet.microsoft.com/download/dotnet/9.0)
- [Discord Developer Portal](https://discord.com/developers/applications)
- [Stripe Dashboard](https://dashboard.stripe.com/)

### 2. Instalação

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd stripe-bot
   ```

2. **Restaure as dependências:**
   ```bash
   dotnet restore
   ```

3. **Configure o arquivo `appsettings.json`:**
   Crie o arquivo `appsettings.json` na raiz do projeto:
   ```json
   {
     "DiscordToken": "SEU_BOT_TOKEN_AQUI",
     "DiscordGuildId": "ID_DO_SEU_SERVIDOR_DISCORD",
     "Stripe": {
       "SecretKey": "sk_test_sua_stripe_secret_key",
       "WebhookSecret": "whsec_seu_webhook_secret"
     },
     "PlanMapping": {
       "premium": "price_id_do_plano_premium",
       "vip": "price_id_do_plano_vip", 
       "pro": "price_id_do_plano_pro"
     },
     "RoleMapping": {
       "price_id_do_plano_premium": "ID_DO_CARGO_PREMIUM",
       "price_id_do_plano_vip": "ID_DO_CARGO_VIP",
       "price_id_do_plano_pro": "ID_DO_CARGO_PRO"
     }
   }
   ```

4. **Configure o webhook no Stripe:**
   - Acesse o [Stripe Dashboard](https://dashboard.stripe.com/webhooks)
   - Crie um novo webhook endpoint: `https://seu-dominio.com/api/stripe-webhook`
   - Selecione os eventos: `checkout.session.completed` e `customer.subscription.deleted`
   - Copie o webhook secret para o arquivo de configuração

### 3. Execução

#### Desenvolvimento:
```bash
# Executar em modo de desenvolvimento
dotnet run

# Ou executar com watch (recompila automaticamente)
dotnet watch run
```

#### Produção:
```bash
# Compilar para produção
dotnet build --configuration Release

# Publicar aplicação
dotnet publish --configuration Release --output ./publish

# Executar aplicação publicada
dotnet ./publish/ApiStripe.dll
```

#### Usando VS Code Tasks:
```bash
# Compilar
dotnet build

# Executar em modo watch
dotnet watch run

# Publicar
dotnet publish
```

## Como Usar

### Para Usuários Discord:

1. **Comprar um plano:**
   - Digite `/comprar plano premium` (ou vip, pro)
   - O bot enviará um link de pagamento no seu privado
   - Complete o pagamento no Stripe
   - Você receberá o cargo automaticamente após o pagamento

### Para Administradores:

1. **Configurar planos no Stripe:**
   - Crie produtos e preços no Stripe Dashboard
   - Adicione os price IDs no arquivo `appsettings.json`

2. **Configurar cargos no Discord:**
   - Crie os cargos no seu servidor Discord
   - Adicione os IDs dos cargos no mapeamento de configuração
   - Certifique-se que o bot tem permissão para gerenciar cargos

3. **Monitorar logs:**
   - Verifique os logs da aplicação para acompanhar transações
   - Use o Swagger UI (em desenvolvimento) para testar endpoints

### Estrutura do Banco de Dados:

A aplicação usa SQLite com a seguinte estrutura:

**Tabela UserSubscriptions:**
- `StripeSubscriptionId` (PK) - ID da assinatura no Stripe
- `DiscordUserId` - ID do usuário no Discord
- `StripeCustomerId` - ID do cliente no Stripe

### URLs Importantes:

- **API Base**: `http://localhost:5000` (desenvolvimento)
- **Swagger UI**: `http://localhost:5000/swagger`
- **Webhook Endpoint**: `http://localhost:5000/api/stripe-webhook`

### Troubleshooting:

- **Bot não responde**: Verifique se o token Discord está correto
- **Pagamentos não processam**: Confirme webhook secret e endpoint
- **Cargos não são atribuídos**: Verifique permissões do bot e IDs dos cargos
- **Erro de banco**: O SQLite é criado automaticamente na primeira execução

-------