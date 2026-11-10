# 🤯 HEAD

> Une référence complète et tenue à jour des éléments `<head>` en HTML — balises meta, relations de lien, icônes, cartes sociales, règles de spéculation et directives pour les moteurs de recherche.

[![CC0](https://img.shields.io/badge/licence-CC0-green.svg?style=for-the-badge)](https://creativecommons.org/publicdomain/zero/1.0/deed.fr)
[![Maintenu par David Corroy](https://img.shields.io/badge/maintenu_par-David_Corroy-0b5fff?style=for-the-badge)](https://david-corroy.com)

**Lire dans une autre langue :** [English](./README.md) · [Español](./README.es.md)

Maintenu par [David Corroy](https://david-corroy.com), consultant SEO. Chaque balise est vérifiée dans sa spécification à jour avant d'être documentée, et tout ce qui a été remplacé part dans [DEPRECATED.md](./DEPRECATED.md) avec le nom de son remplaçant.

## Table des matières

- [Minimum recommandé](#minimum-recommandé)
- [Éléments](#éléments)
- [Ordre recommandé](#ordre-recommandé)
- [Meta](#meta)
- [Link](#link)
- [Scripts](#scripts)
- [Règles de spéculation](#règles-de-spéculation)
- [Extraits de recherche et réponses IA](#extraits-de-recherche-et-réponses-ia)
- [Icônes](#icônes)
- [Social](#social)
  - [Open Graph](#open-graph)
  - [Schema.org](#schemaorg)
  - [JSON-LD pour Google](#json-ld-pour-google)
  - [Pinterest](#pinterest)
  - [OEmbed](#oembed)
  - [QQ/WeChat](#qqwechat)
  - [Dublin Core](#dublin-core)
  - [Fédiverse](#fédiverse)
- [Navigateurs et plateformes](#navigateurs-et-plateformes)
  - [Apple iOS](#apple-ios)
  - [Google Android](#google-android)
  - [Google Chrome](#google-chrome)
- [Navigateurs chinois](#navigateurs-chinois)
  - [Navigateur 360](#navigateur-360)
  - [QQ Mobile Browser](#qq-mobile-browser)
  - [UC Mobile Browser](#uc-mobile-browser)
- [App Links](#app-links)
- [Obsolète](#obsolète)
- [Autres ressources](#autres-ressources)
- [Projets liés](#projets-liés)
- [Traductions](#-traductions)
- [Contribuer](#-contribuer)
- [Auteur](#-auteur)
- [Soutenir](#-soutenir)
- [Licence](#-licence)

## Minimum recommandé

Voici les éléments indispensables à tout document web, site ou application :

```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!--
  Ces deux balises doivent apparaître le plus tôt possible dans le <head>
  pour garantir un rendu correct du document.
  Tout autre élément du head doit venir *après* elles.
-->
<title>Titre de la page</title>
```

`meta charset` — définit l'encodage du site ; `utf-8` est le standard.

`meta name="viewport"` — réglages de la zone d'affichage, liés à l'adaptation mobile.

`width=device-width` — utilise la largeur physique de l'appareil, indispensable sur mobile.

`initial-scale=1` — le zoom initial ; `1` signifie aucun zoom.

## Éléments

Les éléments valides dans un `<head>` sont `meta`, `link`, `title`, `style`, `script`, `noscript` et `base`.

Ils indiquent comment le document doit être interprété et affiché par les technologies du web : navigateurs, moteurs de recherche, robots.

```html
<!--
  Définit l'encodage des caractères du document, pour que
  tous les caractères de l'espace UTF-8 (les emoji, par exemple)
  s'affichent correctement.
-->
<meta charset="utf-8">

<!-- Définit le titre du document -->
<title>Titre de la page</title>

<!-- Définit l'URL de base de toutes les URL relatives du document -->
<base href="https://example.com/page.html">

<!-- Lien vers une feuille de style externe -->
<link rel="stylesheet" href="styles.css">

<!-- Sert à écrire du CSS directement dans le document -->
<style>
  /* ... */
</style>

<!-- Balises JavaScript et sans JavaScript -->
<script src="script.js"></script>
<script>
  // les fonctions vont ici
</script>
<noscript>
  <!-- Solution de repli sans JavaScript -->
</noscript>
```

## Ordre recommandé

Voici l'ordre conseillé des éléments du `<head>`, pour de meilleures performances et un rendu correct :

1. `<meta charset>` — déclaration d'encodage ; elle **doit** figurer dans les 1024 premiers octets du document
2. `<meta name="viewport">` — zone d'affichage ; à déclarer tôt pour un rendu adaptatif correct
3. `<title>` — titre du document, placé après l'encodage et la zone d'affichage pour éviter un nouveau rendu
4. Les autres balises `<meta>` (description, robots, etc.)
5. Les balises Open Graph et sociales
6. `<link rel="canonical">` et les autres balises `<link>`, hors feuilles de style et indices de ressources
7. `<link rel="preconnect">` et `<link rel="dns-prefetch">` — les indices de ressources, tôt pour en tirer le maximum
8. `<link rel="stylesheet">` — le CSS externe ; les feuilles de style passent avant les scripts
9. `<link rel="icon">` — les favicons
10. `<script>` — les scripts ; utilisez `defer` ou `async` dès que possible pour ne pas bloquer le rendu

```html
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>Titre de la page</title>

  <meta name="description" content="Description de la page">
  <!-- autres balises meta -->

  <!-- Balises Open Graph et sociales -->
  <meta property="og:title" content="Titre de la page">
  <!-- autres balises sociales -->

  <link rel="canonical" href="https://example.com/page.html">
  <!-- autres balises link, hors feuilles de style et indices de ressources -->

  <link rel="preconnect" href="https://example.com">
  <link rel="dns-prefetch" href="https://example.com">

  <link rel="stylesheet" href="styles.css">

  <link rel="icon" href="favicon.ico">

  <script defer src="script.js"></script>
</head>
```

## Meta

```html
<!--
  Ces deux balises doivent apparaître le plus tôt possible dans le <head>
  pour garantir un rendu correct du document.
  Tout autre élément du head doit venir *après* elles.
-->
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<!--
  Contrôle les origines autorisées à fournir des ressources.
  À placer le plus tôt possible dans le <head> : la balise ne
  s'applique qu'aux ressources déclarées après elle.
-->
<meta http-equiv="Content-Security-Policy" content="default-src 'self'">

<!-- Nom de l'application web (à n'utiliser que si le site est utilisé comme une application) -->
<meta name="application-name" content="Nom de l'application">

<!-- Couleur de thème pour Chrome, Firefox OS et Opera -->
<meta name="theme-color" content="#4285f4">

<!-- Une couleur de thème par schéma de couleurs ; le navigateur retient celle qui correspond -->
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0b0b0b" media="(prefers-color-scheme: dark)">

<!-- Indique les schémas de couleurs pris en charge par la page (clair, sombre, ou les deux) -->
<meta name="color-scheme" content="light dark">

<!-- Description courte du document (150 caractères maximum) -->
<!-- Ce contenu *peut* être repris dans les résultats des moteurs de recherche. -->
<meta name="description" content="Une description de la page">

<!-- Contrôle l'exploration et l'indexation par les moteurs de recherche -->
<meta name="robots" content="index,follow"><!-- Tous les moteurs -->
<meta name="googlebot" content="index,follow"><!-- Google uniquement -->

<!--
  Contrôle ce que les moteurs ont le droit d'afficher de la page.
  Ces directives conditionnent aussi l'éligibilité à Google Discover
  et aux aperçus enrichis : un grand aperçu d'image est exigé par Discover.
-->
<meta name="robots" content="max-snippet:-1, max-image-preview:large, max-video-preview:-1">

<!-- Demande à Google de ne pas afficher la boîte de recherche des liens de site -->
<meta name="google" content="nositelinkssearchbox">

<!-- Demande à Google de ne pas proposer de traduction de ce document -->
<meta name="google" content="notranslate">

<!-- Vérification de propriété du site -->
<meta name="google-site-verification" content="jeton_de_verification"><!-- Google Search Console -->
<meta name="yandex-verification" content="jeton_de_verification"><!-- Yandex Webmasters -->
<meta name="msvalidate.01" content="jeton_de_verification"><!-- Bing Webmaster Center -->
<meta name="p:domain_verify" content="code_fourni_par_pinterest"><!-- Console Pinterest -->
<meta name="norton-safeweb-site-verification" content="code_norton"><!-- Norton Safe Web -->

<!-- Identifie le logiciel qui a produit le document (WordPress, Dreamweaver, etc.) -->
<meta name="generator" content="programme">

<!-- Description courte du sujet du document -->
<meta name="subject" content="sujet du document">

<!-- Classification générale par âge, selon le contenu du document -->
<meta name="rating" content="General">

<!-- Contrôle la transmission de l'adresse référente -->
<meta name="referrer" content="no-referrer">

<!-- Désactive la détection et la mise en forme automatiques des numéros de téléphone -->
<meta name="format-detection" content="telephone=no">

<!-- Balises géographiques -->
<meta name="ICBM" content="latitude, longitude"><!-- Coordonnées géographiques en degrés décimaux ; ex. content="48.8566, 2.3522" -->
<meta name="geo.position" content="latitude;longitude"><!-- Coordonnées géographiques ; latitude et longitude séparées par un point-virgule -->
<meta name="geo.region" content="pays[-région]"><!-- Code pays (ISO 3166-1) obligatoire, code région (ISO 3166-2) facultatif ; ex. content="FR" / content="FR-75" -->
<meta name="geo.placename" content="ville"><!-- ex. content="Paris" -->

<!-- Web Monetization https://webmonetization.org/docs/getting-started -->
<meta name="monetization" content="$pointeurdepaiement.example">
```

**Remarque :** les balises géographiques ne sont **pas** exploitées directement par les navigateurs. Elles s'adressent aux moteurs de recherche, aux robots d'exploration et aux services de géolocalisation, pour établir la pertinence géographique d'une page. `ICBM` (nommée d'après la convention d'adresse militaire du même nom) et `geo.position` expriment toutes deux des coordonnées en degrés décimaux ; `ICBM` sépare par une virgule, `geo.position` par un point-virgule. `geo.region` identifie le pays et, facultativement, la région, par leurs codes ISO ; `geo.placename` donne un nom de lieu lisible.

- 📖 [Les balises meta comprises par Google](https://developers.google.com/search/docs/crawling-indexing/special-tags?hl=fr)
- 📖 [WHATWG Wiki : MetaExtensions](https://wiki.whatwg.org/wiki/MetaExtensions)
- 📖 [ICBM sur Wikipédia](https://en.wikipedia.org/wiki/ICBM_address#Modern_use)
- 📖 [Géomarquage sur Wikipédia](https://en.wikipedia.org/wiki/Geotagging#HTML_pages)

## Link

```html
<!-- Désigne une feuille de style externe -->
<link rel="stylesheet" href="https://example.com/styles.css">

<!-- Évite les problèmes de contenu dupliqué -->
<link rel="canonical" href="https://example.com/article/?page=2">

<!-- Désigne un manifeste d'application web — la façon recommandée de déclarer les métadonnées d'une PWA : nom, icônes, theme_color, mode d'affichage -->
<link rel="manifest" href="manifest.json">

<!-- Renvoie vers des informations sur le ou les auteurs du document -->
<link rel="author" href="humans.txt">

<!-- Désigne la mention de droits d'auteur applicable au contexte du lien -->
<link rel="license" href="copyright.html">

<!-- Indique une version du document dans une autre langue -->
<link rel="alternate" href="https://es.example.com/" hreflang="es">

<!-- Donne des informations sur un auteur ou une personne.
     Utilisé par RelMeAuth, une forme décentralisée de vérification d'identité.
     Voir https://microformats.org/wiki/RelMeAuth -->
<link rel="me" href="https://google.com/profiles/thenextweb" type="text/html">
<link rel="me" href="mailto:nom@example.com">
<link rel="me" href="sms:+33600000000">

<!-- Auto-référence : utile quand le document est accessible par plusieurs adresses -->
<link rel="self" type="application/atom+xml" href="https://example.com/atom.xml">

<!-- Documents précédent et suivant dans une série -->
<link rel="prev" href="https://example.com/article/?page=1">
<link rel="next" href="https://example.com/article/?page=3">

<!-- Notifie une URL lorsque vous la citez dans votre document
     Plus d'informations sur https://webmention.net -->
<link rel="webmention" href="https://example.com/webmention">

<!-- Permet de publier sur votre propre domaine depuis un client Micropub
     Plus d'informations sur https://indieweb.org/Micropub -->
<link rel="micropub" href="https://example.com/micropub">

<!-- Permet d'utiliser IndieAuth, une solution d'identité qui vous
     authentifie par votre nom de domaine.
     Voir https://indieauth.net -->
<link rel="token_endpoint" href="https://example.com/token">
<link rel="authorization_endpoint" href="https://example.com/auth">

<!-- OpenSearch -->
<link rel="search" href="/open-search.xml" type="application/opensearchdescription+xml" title="Titre de la recherche">

<!-- Flux -->
<link rel="alternate" href="https://feeds.feedburner.com/example" type="application/rss+xml" title="RSS">
<link rel="alternate" href="https://example.com/feed.atom" type="application/atom+xml" title="Atom 0.3">

<!-- Préchargement, préconnexion, prélecture -->
<!-- Plus d'informations : https://css-tricks.com/prefetching-preloading-prebrowsing/ -->
<link rel="dns-prefetch" href="//example.com/">
<link rel="preconnect" href="https://www.example.com/">
<link rel="prefetch" href="https://www.example.com/">

<link rel="preload" href="image.png" as="image">

<!-- Monte ou baisse la priorité d'une ressource préchargée -->
<link rel="preload" href="hero.avif" as="image" fetchpriority="high">

<!-- Précharge un module ES et tout son graphe de dépendances, sans l'exécuter -->
<link rel="modulepreload" href="/js/app.js">
```

**Remarque :** le [manifeste d'application web](https://developer.mozilla.org/fr/docs/Web/Progressive_web_apps/Manifest) (`manifest.json`) est la façon recommandée et multiplateforme de déclarer les propriétés d'une application installable — `name`, `icons`, `theme_color`, mode `display` — dans un seul fichier, plutôt qu'en multipliant les balises `<meta>` propres à chaque plateforme.

- 📖 [Relations de lien (IANA)](https://www.iana.org/assignments/link-relations/link-relations.xhtml)
- 📖 [Manifeste d'application web (MDN)](https://developer.mozilla.org/fr/docs/Web/Progressive_web_apps/Manifest)

## Scripts

```html
<!--
  Scripts : placez les balises <script> en fin de <body> quand c'est possible.
  Les attributs suivants déterminent le comportement de chargement dans le <head> :
-->

<!-- Bloque l'analyse du HTML et le rendu jusqu'à ce que le script soit téléchargé et exécuté -->
<script src="script.js"></script>

<!-- Le script est téléchargé en parallèle de l'analyse et exécuté dès qu'il est disponible, avant la fin de l'analyse -->
<script async src="script.js"></script>

<!-- Le script est téléchargé en parallèle de l'analyse et exécuté une fois la page entièrement analysée -->
<script defer src="script.js"></script>

<!-- async l'emporte dans les navigateurs modernes ; defer sert de repli pour les anciens qui ne gèrent pas async -->
<script async defer src="script.js"></script>

<!-- Script écrit directement dans le document -->
<script>
  // les fonctions vont ici
</script>

<!-- Intégrité des sous-ressources (SRI) : l'attribut integrity vérifie que la ressource n'a pas été altérée en chemin -->
<script src="https://example.com/script.js" integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC"></script>
```

- 📖 [async contre defer](https://www.growingwiththeweb.com/2014/02/async-vs-defer-attributes.html)
- 📖 [Intégrité des sous-ressources (MDN)](https://developer.mozilla.org/fr/docs/Web/Security/Subresource_Integrity)

## Règles de spéculation

Les règles de spéculation indiquent au navigateur les documents que l'internaute a des chances d'ouvrir ensuite, pour qu'il les précharge, voire les préaffiche, avant le clic. Elles se déclarent dans le `<head>`, dans un bloc de script JSON.

```html
<script type="speculationrules">
{
  "prerender": [
    {
      "where": {
        "and": [
          { "href_matches": "/*" },
          { "not": { "href_matches": "/deconnexion" } },
          { "not": { "selector_matches": ".no-prerender" } },
          { "not": { "selector_matches": "[rel~=nofollow]" } }
        ]
      },
      "eagerness": "moderate"
    }
  ],
  "prefetch": [
    {
      "urls": ["page-2.html", "page-3.html"],
      "requires": ["anonymous-client-ip-when-cross-origin"],
      "referrer_policy": "no-referrer"
    }
  ]
}
</script>
```

`eagerness` accepte `immediate`, `eager`, `moderate` et `conservative`, du plus au moins spéculatif. `moderate` se déclenche au survol, `conservative` à l'enfoncement du bouton.

Deux choses à savoir avant de mettre ça en production :

- **Une page préaffichée exécute son JavaScript.** L'analytique, les appels publicitaires et les tests A/B peuvent donc partir pour une visite qui n'aura jamais lieu. Conditionnez-les à `document.prerendering` et à l'événement `prerenderingchange`.
- **Excluez tout ce qui a un effet de bord :** déconnexion, ajout au panier, actions en un clic. Les règles `where` ci-dessus sont là pour ça.

- 📖 [API Speculation Rules (MDN)](https://developer.mozilla.org/fr/docs/Web/API/Speculation_Rules_API)
- 📖 [Préaffichage des pages dans Chrome](https://developer.chrome.com/docs/web-platform/prerender-pages)

## Extraits de recherche et réponses IA

Ce qu'un moteur de recherche, ou un moteur de réponse, a le droit de reproduire de votre page se contrôle par les directives d'extrait. Il n'existe pas de balise dédiée.

```html
<!-- Aucun extrait de texte pour cette page -->
<meta name="robots" content="nosnippet">

<!-- Limite l'extrait à 160 caractères ; -1 signifie sans limite -->
<meta name="robots" content="max-snippet:160">

<!-- Grand aperçu d'image : indispensable pour être éligible à Google Discover -->
<meta name="robots" content="max-image-preview:large">
```

Dans le corps du document, `data-nosnippet` exclut un élément précis de l'extrait :

```html
<p>Visible par tout le monde. <span data-nosnippet>Jamais repris dans les résultats.</span></p>
```

**Aucune balise du `<head>` ne gouverne l'entraînement des modèles ni les réponses des IA.** Ces contrôles se trouvent dans le `robots.txt`, par des jetons d'agent comme `Google-Extended`, `GPTBot`, `PerplexityBot` et `CCBot`, ainsi que par la proposition Content Signals. À noter : `Google-Extended` concerne Gemini et l'ancrage de Vertex AI — il n'a aucun effet sur Google Search, ni sur les AI Overviews, qui dépendent de Googlebot et des directives d'extrait ci-dessus.

- 📖 [Balises et attributs compris par Google](https://developers.google.com/search/docs/crawling-indexing/special-tags?hl=fr)
- 📖 [Google-Extended](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers?hl=fr#google-extended)

## Icônes

```html
<!-- Pour Internet Explorer 10 et antérieurs -->
<!-- Placez favicon.ico à la racine — aucune balise nécessaire -->

<!-- L'icône dans la plus haute résolution utile -->
<link rel="icon" sizes="192x192" href="/chemin/vers/icone.png">

<!-- Icône tactile Apple (réutilise l'icône 192 px) -->
<link rel="apple-touch-icon" href="/chemin/vers/apple-touch-icon.png">
```

- 📖 [Tout sur les favicons et les icônes tactiles](https://bitsofco.de/all-about-favicons-and-touch-icons/)
- 📖 [Aide-mémoire des favicons](https://github.com/audreyfeldroy/favicon-cheat-sheet)
- 📖 [Icônes et couleurs de navigateur](https://web.dev/articles/icons-and-browser-colors)

## Social

### Open Graph

> Le [protocole Open Graph](https://ogp.me/) est le standard de fait pour contrôler l'apparence de vos contenus lorsqu'ils sont partagés. Créé à l'origine par Facebook, il est aujourd'hui exploité par la plupart des grandes plateformes : LinkedIn, X (en repli quand les balises Twitter Card sont absentes), Discord, Slack, iMessage, Mastodon, Bluesky et WhatsApp.

```html
<meta property="og:url" content="https://example.com/page.html">
<meta property="og:type" content="website">
<meta property="og:title" content="Titre du contenu">
<meta property="og:image" content="https://example.com/image.jpg">
<meta property="og:image:alt" content="Description de ce que montre l'image, et non une légende">
<meta property="og:description" content="Description ici">
<meta property="og:site_name" content="Nom du site">
<meta property="og:locale" content="fr_FR">
<meta property="article:author" content="">
```

- 📖 [Protocole Open Graph](https://ogp.me/)
- 🛠 Testez votre page avec le [débogueur de partage Facebook](https://developers.facebook.com/tools/debug/) ou le [Post Inspector de LinkedIn](https://www.linkedin.com/post-inspector/)

### Schema.org

```html
<html lang="" itemscope itemtype="https://schema.org/Article">
    <head>
      <link rel="author" href="">
      <link rel="publisher" href="">
      <meta itemprop="name" content="Titre du contenu">
      <meta itemprop="description" content="Description du contenu, moins de 200 caractères">
      <meta itemprop="image" content="https://example.com/image.jpg">
```

**Remarque :** ces balises exigent que les attributs `itemscope` et `itemtype` soient portés par la balise `<html>`.

- 📖 [Premiers pas — schema.org](https://schema.org/docs/gs.html)
- 🛠 Testez votre page avec le [test des résultats enrichis](https://search.google.com/test/rich-results?hl=fr)

### JSON-LD pour Google

Ce balisage aide Google à produire un panneau de graphe de connaissances pour votre marque — l'encadré qui apparaît à droite des résultats, le plus souvent pour les marques établies.

```html
<script type="application/ld+json">
  {
    "@context": "http://schema.org",
    "@type": "Organization",
    "name": "votremarque.com",
    "url": "https://www.votremarque.com/",
    "logo": "https://www.votremarque.com/logo.png",
    "sameAs": [
      "https://www.facebook.com/votremarque",
      "https://twitter.com/votremarque",
      "https://fr.pinterest.com/votremarque/",
      "https://www.instagram.com/votremarque/",
      "https://www.linkedin.com/company/votremarque"
    ]
  }
</script>
```

### Pinterest

Pinterest permet d'empêcher l'enregistrement de contenus depuis votre site, [selon son centre d'aide](https://help.pinterest.com/fr/business/article/prevent-saves-to-pinterest-from-your-site). L'attribut `description` est facultatif.

```html
<meta name="pinterest" content="nopin" description="Désolé, on n'enregistre pas depuis ce site.">
```

### OEmbed

```html
<link rel="alternate" type="application/json+oembed"
  href="https://example.com/services/oembed?url=http%3A%2F%2Fexample.com%2Ffoo%2F&amp;format=json"
  title="Profil oEmbed : JSON">
<link rel="alternate" type="text/xml+oembed"
  href="https://example.com/services/oembed?url=http%3A%2F%2Fexample.com%2Ffoo%2F&amp;format=xml"
  title="Profil oEmbed : XML">
```

- 📖 [Format oEmbed](https://oembed.com/)

### QQ/WeChat

Les pages partagées vers QQ et WeChat s'affichent sous forme de message mis en forme.

```html
<meta itemprop="name" content="titre du partage">
<meta itemprop="image" content="http://imgcache.qq.com/qqshow/ac/v4/global/logo.png">
<meta name="description" itemprop="description" content="contenu du partage">
```

- 📖 [Documentation du format](https://open.mobile.qq.com/api/mqq/index#api:setShareInfo)

### Dublin Core

Le [Dublin Core](https://www.dublincore.org/) est un vocabulaire de métadonnées normalisé sous la référence [ISO 15836](https://www.iso.org/standard/71339.html) et maintenu par la Dublin Core Metadata Initiative. Il définit quinze éléments pour décrire une ressource et reste très utilisé dans les bibliothèques numériques, les dépôts institutionnels, l'édition scientifique et les portails publics. Pour l'employer en HTML, déclarez l'espace de noms DC, puis ajoutez les éléments voulus en balises `<meta>` préfixées par `DC.`.

```html
<!-- Déclaration de l'espace de noms Dublin Core -->
<link rel="schema.DC" href="https://purl.org/dc/elements/1.1/">

<meta name="DC.title" content="Titre de la page">
<meta name="DC.creator" content="Nom de l'auteur">
<meta name="DC.subject" content="Mots-clés ; thèmes">
<meta name="DC.description" content="Brève description du contenu de la page">
<meta name="DC.publisher" content="Nom de l'éditeur">
<meta name="DC.contributor" content="Nom du contributeur">
<meta name="DC.date" content="AAAA-MM-JJ">
<meta name="DC.type" content="Text">
<meta name="DC.format" content="text/html">
<meta name="DC.identifier" content="https://example.com/page.html">
<meta name="DC.source" content="https://example.com/source-originale">
<meta name="DC.language" content="fr">
<meta name="DC.relation" content="https://example.com/ressource-liee">
<meta name="DC.coverage" content="Couverture géographique ou temporelle">
<meta name="DC.rights" content="Titulaire des droits">
```

- 📖 [Dublin Core Metadata Element Set](https://www.dublincore.org/specifications/dublin-core/dces/)
- 📖 [Utiliser le Dublin Core en HTML](https://www.dublincore.org/specifications/dublin-core/dcq-html/)

### Fédiverse

Certains logiciels du fédiverse, Mastodon notamment, permettent de déclarer votre identifiant dans une balise meta, qui apparaîtra alors dans les aperçus de vos pages. En plus de la balise, il faut ajouter votre domaine à la liste des sites autorisés : « Préférences → Profil public → Vérification → Attribution d'auteur » sur Mastodon.

```html
<meta name="fediverse:creator" content="@identifiant@example.org">
```

## Navigateurs et plateformes

### Apple iOS

```html
<!-- Bandeau Smart App Banner -->
<meta name="apple-itunes-app" content="app-id=APP_ID,affiliate-data=AFFILIATE_ID,app-argument=TEXTE">

<!-- Désactive la détection et la mise en forme automatiques des numéros de téléphone -->
<meta name="format-detection" content="telephone=no">

<!-- Icône de lancement (180 × 180 px ou plus) -->
<link rel="apple-touch-icon" href="/chemin/vers/apple-touch-icon.png">

<!-- Image de l'écran de lancement -->
<link rel="apple-touch-startup-image" href="/chemin/vers/lancement.png">

<!-- Titre de l'icône de lancement -->
<meta name="apple-mobile-web-app-title" content="Titre de l'application">

<!-- Active le mode autonome, en plein écran -->
<meta name="mobile-web-app-capable" content="yes">

<!-- Apparence de la barre d'état (sans effet si le mode autonome n'est pas activé) -->
<meta name="apple-mobile-web-app-status-bar-style" content="black">

<!-- Adaptation aux écrans à encoche (iPhone X et suivants) ; ajoutez viewport-fit=cover à votre balise viewport existante -->
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">

<!-- Liens profonds vers une application iOS -->
<meta name="apple-itunes-app" content="app-id=APP-ID, app-argument=http/url-exemple.com">
<link rel="alternate" href="ios-app://APP-ID/http/url-exemple.com">
```

- 📖 [Configuring Web Applications (Apple)](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html)

**Remarque :** le titre de l'application (`apple-mobile-web-app-title`), le mode d'affichage et les icônes (`apple-touch-icon`) se configurent plus sûrement, et de façon portable, par le [manifeste d'application web](https://developer.mozilla.org/fr/docs/Web/Progressive_web_apps/Manifest) (`<link rel="manifest">`), qui est la méthode recommandée pour une PWA. Les balises propres à Apple restent utiles en repli pour les anciennes versions d'iOS.

### Google Android

```html
<meta name="theme-color" content="#E64545">

<!-- Ajout à l'écran d'accueil -->
<meta name="mobile-web-app-capable" content="yes">
<!-- Plus d'informations : https://developer.chrome.com/multidevice/android/installtohomescreen -->

<!-- Liens profonds vers une application Android -->
<meta name="google-play-app" content="app-id=nom-du-paquet">
<link rel="alternate" href="android-app://nom-du-paquet/http/url-exemple.com">
```

**Remarque :** `theme-color` et le comportement « ajouter à l'écran d'accueil » se définissent mieux par le [manifeste d'application web](https://developer.mozilla.org/fr/docs/Web/Progressive_web_apps/Manifest) (`<link rel="manifest">`). La balise `theme-color` garde son utilité en repli pour les navigateurs qui ne gèrent pas encore la propriété `theme_color` du manifeste.

### Google Chrome

```html
<link rel="chrome-webstore-item" href="https://chrome.google.com/webstore/detail/APP_ID">

<!-- Désactive la proposition de traduction -->
<meta name="google" content="notranslate">
```

## Navigateurs chinois

### Navigateur 360

```html
<!-- Choisit l'ordre des moteurs de rendu -->
<meta name="renderer" content="webkit|ie-comp|ie-stand">
```

### QQ Mobile Browser

```html
<!-- Verrouille l'écran dans l'orientation indiquée -->
<meta name="x5-orientation" content="landscape/portrait">

<!-- Affiche le document en plein écran -->
<meta name="x5-fullscreen" content="true">

<!-- Affiche le document en « mode application » : plein écran, etc. -->
<meta name="x5-page-mode" content="app">
```

### UC Mobile Browser

```html
<!-- Verrouille l'écran dans l'orientation indiquée -->
<meta name="screen-orientation" content="landscape/portrait">

<!-- Affiche le document en plein écran -->
<meta name="full-screen" content="yes">

<!-- UC affiche les images même en « mode texte » -->
<meta name="imagemode" content="force">

<!-- Affiche le document en « mode application » : plein écran, gestes désactivés, etc. -->
<meta name="browsermode" content="application">

<!-- Désactive le « mode nuit » d'UC pour ce document -->
<meta name="nightmode" content="disable">

<!-- Simplifie le document pour réduire le volume de données -->
<meta name="layoutmode" content="fitscreen">

<!-- Désactive l'agrandissement automatique de la police sur les documents très chargés en texte -->
<meta name="wap-font-scale" content="no">
```

- 📖 [Documentation UC Browser](https://www.uc.cn/download/UCBrowser_U3_API.doc)

## App Links

```html
<!-- iOS -->
<meta property="al:ios:url" content="applinks://docs">
<meta property="al:ios:app_store_id" content="12345">
<meta property="al:ios:app_name" content="App Links">

<!-- Android -->
<meta property="al:android:url" content="applinks://docs">
<meta property="al:android:app_name" content="App Links">
<meta property="al:android:package" content="org.applinks">

<!-- Repli web -->
<meta property="al:web:url" content="https://applinks.org/documentation">
```

- 📖 [App Links](https://developers.facebook.com/docs/applinks)

## Obsolète

Pour les balises et les éléments qui ont fait partie de ce guide mais ne sont plus pris en charge — compatibilité Internet Explorer, onglets épinglés de Safari, balise `view-transition`, vérification Alexa, etc. — voir [DEPRECATED.md](./DEPRECATED.md).

## Autres ressources

- 📖 [HTML5 Boilerplate : le HTML](https://github.com/h5bp/html5-boilerplate/blob/main/docs/html.md)
- 📖 [HTML5 Boilerplate : étendre et personnaliser](https://github.com/h5bp/html5-boilerplate/blob/main/docs/extend.md)

## Projets liés

- [head-it](https://github.com/hemanth/head-it) — interface en ligne de commande pour les extraits `<head>`
- [Sublime Text HTML Head Snippets](https://github.com/marcobiedermann/sublime-head-snippets) — extraits `<head>` pour Sublime Text
- [vue-head](https://github.com/ktquez/vue-head) — gestion des métadonnées du `<head>` dans Vue.js

## 🌐 Traductions

- [English](./README.md)
- [Español](./README.es.md)

## 🤝 Contribuer

**Ouvrez un ticket ou une demande de fusion pour proposer un ajout ou une correction.**

Conventions à respecter :

- Ne modifiez qu'une balise, ou qu'un ensemble cohérent de balises, à la fois
- Utilisez des guillemets doubles pour les attributs
- Pas de barre oblique finale sur les éléments auto-fermants : la spécification HTML5 la rend facultative
- Joignez un lien vers la documentation qui appuie votre modification
- Si une balise devient obsolète ou se voit remplacée, déplacez-la dans [DEPRECATED.md](./DEPRECATED.md) au lieu de la supprimer, et nommez son remplaçant

## 👤 Auteur

**David Corroy** — consultant SEO, France.

Je tiens ce guide parce que le `<head>` est l'endroit où se joue la visibilité d'une page, et que la plupart des références sur le sujet ont des années de retard.

- 🌐 Site : [david-corroy.com](https://david-corroy.com)
- 🦊 GitLab : [@david-corroy](https://gitlab.com/david-corroy)
- 🐙 GitHub : [@david-corroy](https://github.com/david-corroy)

## ⭐ Soutenir

Si ce guide vous a fait gagner du temps :

- ⭐ Mettez une étoile, sur [GitLab](https://gitlab.com/david-corroy/head) ou sur [GitHub](https://github.com/david-corroy/HEAD)
- 🗣 Ouvrez un ticket quand vous trouvez une balise manquante, ou une qui ne fait plus rien
- 🔗 Faites un lien vers ce guide plutôt que de le recopier, pour que vos lecteurs aient la version corrigée

## 📝 Licence

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/deed.fr)

Cette œuvre est versée au domaine public sous [CC0 1.0 Universel](./LICENSE). Vous pouvez la copier, la modifier et la diffuser, y compris à des fins commerciales, sans demander d'autorisation.
