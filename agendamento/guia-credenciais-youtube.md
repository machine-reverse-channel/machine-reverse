# Guia: ligar o canal Pickup Reality ao robô de upload

Leva uns 15 minutos. Use a conta Google que é dona do canal Pickup Reality. Nunca cole nenhum código ou senha no chat: tudo vai direto para os Secrets do GitHub.

## Passo 0. Verificar o canal (obrigatório, 2 minutos)
1. Abra https://www.youtube.com/verify logado no canal Pickup Reality.
2. Confirme pelo celular (SMS).
Sem isso o YouTube recusa vídeos com mais de 15 minutos e thumbnails personalizadas. Todos os nossos longos têm 16 a 22 minutos.

## Passo 1. Criar o projeto no Google Cloud
1. Abra https://console.cloud.google.com e clique no seletor de projeto (topo) > **Novo projeto**. Nome: `Pickup Reality Uploader`. Criar.
2. Com o projeto selecionado, abra https://console.cloud.google.com/apis/library/youtube.googleapis.com e clique **Ativar** (YouTube Data API v3).

## Passo 2. Tela de consentimento
1. Abra https://console.cloud.google.com/auth/overview e clique **Começar**.
2. Nome do app: `Pickup Reality Uploader`. E-mail de suporte: o seu. Público: **Externo**. Contato: o seu e-mail. Concluir.
3. Em **Público-alvo** (Audience), clique **Publicar app** (colocar "Em produção"). Isso evita que a autorização expire a cada 7 dias. Vai aparecer um aviso de app não verificado; é normal, só você vai usar.

## Passo 3. Criar a credencial
1. Abra https://console.cloud.google.com/auth/clients > **Criar cliente**.
2. Tipo: **Aplicativo da Web**. Nome: `uploader`.
3. Em **URIs de redirecionamento autorizados**, adicione exatamente: `https://developers.google.com/oauthplayground`
4. Criar. Deixe a janela aberta: ela mostra o **ID do cliente** e a **Chave secreta do cliente**.

## Passo 4. Gerar o token de acesso ao canal
1. Abra https://developers.google.com/oauthplayground
2. Clique na engrenagem (canto superior direito) > marque **Use your own OAuth credentials** > cole o ID do cliente e a Chave secreta.
3. Na caixa da esquerda "Input your own scopes", cole: `https://www.googleapis.com/auth/youtube.force-ssl` e clique **Authorize APIs**.
4. Escolha a conta e, se perguntar, **o canal Pickup Reality** (não o seu canal pessoal). Na tela "app não verificado": Avançado > Acessar (não seguro) > Permitir.
5. De volta ao Playground, clique **Exchange authorization code for tokens**. Copie o **Refresh token**.

## Passo 5. Guardar no GitHub
Abra https://github.com/viniciushoscher-ctrl/american-trucks/settings/secrets/actions > **New repository secret**, três vezes:
- `YT_CLIENT_ID` = ID do cliente
- `YT_CLIENT_SECRET` = Chave secreta do cliente
- `YT_REFRESH_TOKEN` = Refresh token

Depois é só me avisar "secrets prontos" no chat.

## Passo 6. Pedir a auditoria do Google (o passo que libera a publicação automática)
Projetos novos da API ficam travados: todo vídeo enviado pela API fica **privado e não pode ser publicado** até o Google auditar o projeto. Por isso:
1. Abra o formulário "YouTube API Services - Audit and Quota Extension": https://support.google.com/youtube/contact/yt_api_form
2. Marque que é para **auditoria e aumento de quota**. Uso: "Internal tool that uploads and schedules videos to my own channel (Pickup Reality) only. No third-party users."
3. Peça quota de **50.000 unidades/dia** (cada upload custa 1.600; 1 longo + 2 Shorts por dia + thumbnail + legenda ≈ 5.300).
A resposta costuma levar de alguns dias a algumas semanas.
