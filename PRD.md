# PRD — Refatoração do site AICITI

## 1. Visão geral

**Projeto**: Refatoração completa do site institucional da AICITI (Associação das Imobiliárias e Corretores de Imóveis de Tramandaí e Imbé), atualmente em produção em [aiciti.com.br](https://www.aiciti.com.br/).

**Objetivo**: Recriar o site com o mesmo conteúdo e propósito institucional, em uma nova base técnica mais moderna e sustentável, mantendo as informações e funcionalidades já existentes (institucional, benefícios, parceiros, dúvidas, blog e contato).

**Área restrita "Acessos"**: construtoras associadas alimentam tabelas de preços dos seus
empreendimentos, e corretores/imobiliárias associados visualizam essas tabelas — ver seção 12-A.

## 2. Stack técnica

- **Backend**: Django (templates server-side, ORM para posts do blog, mensagens de contato, parceiros e diretoria).
- **Estilo**: Tailwind CSS.
- **Interatividade no client**: Alpine.js (componentes leves: menu mobile, accordion de FAQ, carrossel de logos).
- **Atualizações parciais de página**: HTMX (ex: paginação/filtro do blog, envio do formulário de contato sem reload completo).
- **Admin/CMS**: Django Admin como painel de gestão de conteúdo (posts do blog, parceiros, diretoria, benefícios), evitando a necessidade de um CMS externo.
- **Deploy/Infraestrutura**: aplicação containerizada (Docker), a ser hospedada em uma VPS. A imagem/container deve ser autossuficiente (app Django + assets do Tailwind já buildados), permitindo deploy via `docker run`/`docker compose` na VPS.

## 3. Estrutura global

Todas as páginas do site compartilham:
- **Cabeçalho**: logo da AICITI + barra de menu de navegação (colapsa em menu mobile via Alpine.js).
- **Rodapé**: links rápidos de navegação, redes sociais (Facebook e Instagram), dados de contato resumidos (telefone e endereço).

## 4. Menu de navegação

Ordem e itens do menu principal:

1. Página inicial
2. Sobre
3. Benefícios
4. Parceiros
5. Dúvidas
6. Blog
7. Contato
8. **Acessos** (dropdown com 3 subitens — ver seção 12-A):
   - Área das construtoras
   - Área dos corretores
   - Acesso ao Roll (link externo: `https://tramandai.aiciti.com.br/login?logout`)

## 5. Página Inicial

Seções, na ordem:

1. **Hero** — título "AICITI TDAÍ" + descrição "Associação das Imobiliárias e Corretores de Imóveis de Tramandaí e Imbé", com call-to-action (ex: "Associe-se" ou "Saiba mais").
2. **Sobre nós** — resumo institucional (ver texto completo na seção 6), com link "saiba mais" para a página Sobre.
3. **Imobiliárias associadas** — grid/carrossel com os logos das imobiliárias e corretores associados.
4. **Benefícios para associados** — os 3 benefícios resumidos (título + ícone), com link para a página Benefícios.
5. **Gestores** — apresentação da diretoria atual (nomes e cargos), com link para a página Sobre para o detalhamento completo.
6. **Blog** — cards com os posts mais recentes/em destaque, com link "ver todos" para a página Blog.

## 6. Página Sobre

**Texto institucional** (conteúdo de referência, migrado do site atual):

> A AICITI (Associação das Imobiliárias e Corretores de Imóveis de Tramandaí e Imbé) representa o setor imobiliário de Tramandaí e Imbé, no litoral norte do Rio Grande do Sul. Fundada em 2001, a entidade se dedica a unir as imobiliárias e corretores de imóveis da região, promovendo ética, transparência e profissionalismo no mercado imobiliário local. A associação oferece convênios, benefícios exclusivos, capacitações e eventos para seus associados, além de promover qualificação contínua através de treinamentos e palestras sobre tendências do setor.

**Integrantes da diretoria** (conteúdo de referência):

| Cargo | Nome |
|---|---|
| Presidente | Thiago Kury |
| Vice-Presidente | Marlon Alves |
| 1ª Secretária | Patricia Beck |
| 2º Secretário | Jonas Rosa |
| 1º Tesoureiro | Cicero Severo |
| 2ª Tesoureira | Mana Brochier |

**Membros titulares**: Alfeu Barros, Carlos Henrique, Alessandra Wagner, Danubia Firme, Eduardo Wypyszinski, Indiana Barbosa.

**Membros suplentes**: Rafael Britto, Tiago Schmals, Natascha Motta.

> Nota: confirmar com a AICITI se todos os nomes/cargos acima seguem atuais antes da publicação, e se o item "BOT AICITI" (assistente de IA) presente no site atual deve ser mantido nesta página ou tratado como funcionalidade à parte.

## 7. Página Benefícios

Os 3 benefícios para associados, cada um com título, ícone e descrição:

1. **Descontos em Comércios** — parcerias comerciais com descontos exclusivos para associados.
2. **Site e CRM** — ferramentas digitais disponibilizadas aos associados (presença online e gestão de relacionamento com clientes).
3. **Anúncios e Divulgações** — apoio de marketing e visibilidade para os associados.

> Pendência: o site atual expõe apenas resumos ("Veja Mais") sem detalhar o texto completo de cada benefício. É necessário levantar com a diretoria da AICITI o texto expandido de cada um antes da diagramação final da página.

## 8. Página Parceiros

**Descrição**: As empresas parceiras da AICITI fazem parte de um ecossistema que fortalece o mercado imobiliário de Tramandaí e Imbé.

**Layout**: grid de cards, um por parceiro, contendo:
- Logo do parceiro
- Endereço do site (link externo)
- Ícones de redes sociais do parceiro (Facebook e Instagram)

**Parceiros identificados no site atual** (conteúdo de referência a confirmar/expandir):

- Academia UP
- Panela Food Burger
- Construtora Coruja
- Genuino Construtora
- Construtora Panassolo
- Sardi Galaschi Incorporadora
- Select Construtora e Incorporadora
- Contemporânea Construtora
- LS Administradora Predial
- Constru Matta

> Pendência: o site atual não expõe site nem redes sociais individuais de cada parceiro (apenas os canais da própria AICITI). É necessário coletar essas informações junto a cada parceiro/diretoria antes da publicação.

## 9. Página Dúvidas

Perguntas e respostas migradas do site atual, exibidas em formato de accordion (expandir/recolher via Alpine.js):

1. **O que é a AICITI?**
   Associação das Imobiliárias e Corretores de Imóveis de Tramandaí e Imbé, que representa e fortalece a classe imobiliária regional, promovendo ética profissional e desenvolvimento de mercado.

2. **Quem pode se associar à AICITI?**
   Imobiliárias constituídas legalmente e corretores registrados no CRECI que atuem em Tramandaí e Imbé, incluindo profissionais autônomos.

3. **Quais são as vantagens de ser associado?**
   Acesso a convênios exclusivos, capacitação profissional, eventos de networking, representação institucional e benefícios comerciais.

4. **A AICITI oferece capacitação?**
   Sim, promove palestras, workshops e cursos sobre práticas de mercado, inovação, vendas, legislação e tecnologias imobiliárias.

5. **A associação defende interesses da categoria?**
   A AICITI é representante oficial, atuando junto a entidades públicas e privadas para garantir direitos e promover um mercado justo.

6. **Que tipos de convênios oferece?**
   Assessoria jurídica, cursos com desconto, comunicação/marketing, soluções tecnológicas (CRM) e materiais de divulgação.

7. **Como se associar?**
   Contatar a diretoria, preencher ficha de cadastro, apresentar documentação e aguardar aprovação.

8. **Quais as responsabilidades do associado?**
   Seguir código de ética, atuar com transparência, participar de reuniões e manter contribuições em dia.

9. **A AICITI organiza eventos?**
   Sim, promove encontros periódicos, seminários e feiras que geram networking e compartilham tendências do mercado.

## 10. Página Blog

**Sistema de blog** construído sobre Django:
- Modelo `Post` (título, slug, conteúdo, imagem de capa, data de publicação, autor, status rascunho/publicado).
- Gestão de posts via Django Admin (sem necessidade de painel customizado nesta fase).
- Listagem paginada de posts na página Blog (mais recentes primeiro), com paginação via HTMX.
- Página de post individual com conteúdo completo, compartilhamento em redes sociais (opcional).
- Seção "Blog" da página inicial exibe os posts mais recentes/destaque, puxados do mesmo modelo.

## 11. Página Contato

- **Formulário de contato**: campos nome, e-mail, telefone e mensagem. Envio via HTMX (sem reload da página), processado no backend Django: grava a mensagem no banco e envia notificação por e-mail para a diretoria.
- **Mapa**: mapa incorporado (Google Maps embed) apontando para o endereço da sede (o site atual não possui mapa — esta é uma adição nesta refatoração).
- **Informações de contato**:
  - Endereço: Rua Doze de Abril, 264, Centro, Tramandaí/RS
  - Telefone: (51) 99903.8844
  - Atendimento: somente on-line, via WhatsApp (não há e-mail público divulgado no site atual)
  - Redes sociais: Facebook (@associa.aiciti.3) e Instagram (@aiciti_rs)

## 12-A. Área restrita "Acessos"

**Objetivo**: construtoras associadas cadastram tabelas de preços dos empreendimentos que estão
construindo; corretores e imobiliárias associados visualizam (somente leitura) as tabelas de
todas as construtoras.

**Modelo de dados**:
- `Builder` (construtora): conta vinculada a um `User` do Django, nome e logo. Independente do
  modelo `Partner` já existente (uma construtora pode ou não também ser parceira comercial listada
  na página Parceiros — não há vínculo entre os dois cadastros).
- `PriceTable` (tabela de preços), pertencente a uma `Builder`: nome da tabela, descrição, imagem e
  link para uma pasta de drive.

**Regras de acesso**:
- Construtora: login/senha próprios, só vê e só edita/exclui as tabelas da própria construtora.
- Corretor/imobiliária: login/senha próprios (grupo "Corretores"), acesso somente leitura a todas
  as tabelas de todas as construtoras.
- **Provisionamento 100% manual**: não há autocadastro público. A diretoria da AICITI cria cada
  conta (de construtora ou de corretor/imobiliária) diretamente pelo Django Admin e repassa
  login/senha por fora do site.
- "Acesso ao Roll" é apenas um link externo estático (`https://tramandai.aiciti.com.br/login?logout`,
  sistema de terceiros já existente) — não há nada a construir para esse subitem além do link no
  menu.

## 12. Fora de escopo

- Qualquer integração de pagamento, automação de aprovação de associados, autocadastro público na
  área restrita, ou outras funcionalidades não mencionadas explicitamente neste documento.

## 13. Requisitos não funcionais

- **Responsivo**: layout mobile-first, adequado para visualização em celulares, tablets e desktop.
- **SEO básico**: meta tags (title/description) por página, sitemap.xml, URLs amigáveis para posts do blog.
- **Performance**: otimização de imagens (logos de parceiros/imobiliárias), carregamento rápido do HTMX/Alpine (sem framework JS pesado).
- **Acessibilidade**: contraste adequado, textos alternativos em imagens/logos, navegação por teclado no menu e no accordion de dúvidas.

## 14. Pendências / itens em aberto

- Texto completo (expandido) dos 3 benefícios para associados.
- Dados individuais de cada parceiro: endereço do site e redes sociais (Facebook/Instagram).
- Confirmação da lista atual de diretoria/integrantes junto à AICITI.
- Definição de prazo do projeto.
- Detalhes da VPS de destino (provedor, especificações, acesso) e do processo de deploy (CI/CD manual ou automatizado) do container.
- Decisão sobre inclusão futura do "BOT AICITI" (assistente de IA mencionado no site atual).
- Lista real das construtoras e corretores/imobiliárias que devem receber conta na área restrita
  "Acessos" (nomes e a quem entregar login/senha), para a AICITI provisionar via Django Admin.
