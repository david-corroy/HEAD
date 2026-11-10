# 🤯 HEAD

> Una referencia completa y mantenida de los elementos `<head>` en HTML: etiquetas meta, relaciones de enlace, iconos, tarjetas sociales, reglas de especulación y directivas para buscadores.

[![CC0](https://img.shields.io/badge/licencia-CC0-green.svg?style=for-the-badge)](https://creativecommons.org/publicdomain/zero/1.0/deed.es)
[![Mantenido por David Corroy](https://img.shields.io/badge/mantenido_por-David_Corroy-0b5fff?style=for-the-badge)](https://david-corroy.com)

**Léelo en otro idioma:** [English](./README.md) · [Français](./README.fr.md)

**¿Con prisa?** [`head.html`](./head.html) es un `<head>` completo y comentado, en el orden recomendado, listo para copiar.

Mantenido por [David Corroy](https://david-corroy.com), consultor SEO. Cada etiqueta se comprueba contra su especificación vigente antes de documentarse, y todo lo que ha quedado sustituido pasa a [DEPRECATED.md](./DEPRECATED.md) indicando su reemplazo.

## Tabla de contenidos

- [Mínimo recomendado](#mínimo-recomendado)
- [Elementos](#elementos)
- [Orden recomendado](#orden-recomendado)
- [Meta](#meta)
- [Link](#link)
- [Scripts](#scripts)
- [Reglas de especulación](#reglas-de-especulación)
- [Fragmentos de búsqueda y respuestas de IA](#fragmentos-de-búsqueda-y-respuestas-de-ia)
- [Iconos](#iconos)
- [Social](#social)
  - [Open Graph](#open-graph)
  - [Schema.org](#schemaorg)
  - [JSON-LD para Google](#json-ld-para-google)
  - [Pinterest](#pinterest)
  - [OEmbed](#oembed)
  - [QQ/WeChat](#qqwechat)
  - [Dublin Core](#dublin-core)
  - [Fediverso](#fediverso)
- [Navegadores y plataformas](#navegadores-y-plataformas)
  - [Apple iOS](#apple-ios)
  - [Google Android](#google-android)
  - [Google Chrome](#google-chrome)
- [Navegadores chinos](#navegadores-chinos)
  - [Navegador 360](#navegador-360)
  - [QQ Mobile Browser](#qq-mobile-browser)
  - [UC Mobile Browser](#uc-mobile-browser)
- [App Links](#app-links)
- [Obsoleto](#obsoleto)
- [Otros recursos](#otros-recursos)
- [Proyectos relacionados](#proyectos-relacionados)
- [Traducciones](#-traducciones)
- [Contribuir](#-contribuir)
- [Autor](#-autor)
- [Apoyar](#-apoyar)
- [Licencia](#-licencia)

## Mínimo recomendado

Estos son los elementos imprescindibles en cualquier documento web, sea un sitio o una aplicación:

```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!--
  Estas dos etiquetas deben aparecer lo antes posible dentro del <head>
  para garantizar un renderizado correcto del documento.
  Cualquier otro elemento del head debe ir *después* de ellas.
-->
<title>Título de la página</title>
```

`meta charset` — define la codificación del sitio; `utf-8` es el estándar.

`meta name="viewport"` — ajustes del área visible, relacionados con la adaptación a móviles.

`width=device-width` — usa el ancho físico del dispositivo, imprescindible en móvil.

`initial-scale=1` — el zoom inicial; `1` significa sin zoom.

## Elementos

Los elementos válidos dentro de un `<head>` son `meta`, `link`, `title`, `style`, `script`, `noscript` y `base`.

Indican cómo deben interpretar y mostrar el documento las tecnologías de la web: navegadores, buscadores y robots.

```html
<!--
  Define la codificación de caracteres del documento, para que
  todos los caracteres del espacio UTF-8 (los emoji, por ejemplo)
  se muestren correctamente.
-->
<meta charset="utf-8">

<!-- Define el título del documento -->
<title>Título de la página</title>

<!-- Define la URL base de todas las URL relativas del documento -->
<base href="https://example.com/pagina.html">

<!-- Enlace a una hoja de estilos externa -->
<link rel="stylesheet" href="styles.css">

<!-- Sirve para escribir CSS dentro del propio documento -->
<style>
  /* ... */
</style>

<!-- Etiquetas de JavaScript y de ausencia de JavaScript -->
<script src="script.js"></script>
<script>
  // aquí van las funciones
</script>
<noscript>
  <!-- Alternativa sin JavaScript -->
</noscript>
```

## Orden recomendado

Este es el orden aconsejado de los elementos del `<head>`, para obtener el mejor rendimiento y un renderizado correcto:

1. `<meta charset>` — declaración de codificación; **debe** aparecer dentro de los primeros 1024 bytes del documento
2. `<meta name="viewport">` — área visible; se declara pronto para asegurar un renderizado adaptable correcto
3. `<title>` — título del documento, después de la codificación y el viewport para evitar un nuevo renderizado
4. El resto de etiquetas `<meta>` (description, robots, etc.)
5. Las etiquetas de Open Graph y redes sociales
6. `<link rel="canonical">` y las demás etiquetas `<link>`, salvo hojas de estilo e indicios de recursos
7. `<link rel="preconnect">` y `<link rel="dns-prefetch">` — los indicios de recursos, pronto para aprovecharlos al máximo
8. `<link rel="stylesheet">` — el CSS externo; las hojas de estilo van antes que los scripts
9. `<link rel="icon">` — los favicons
10. `<script>` — los scripts; use `defer` o `async` siempre que pueda para no bloquear el renderizado

```html
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>Título de la página</title>

  <meta name="description" content="Descripción de la página">
  <!-- otras etiquetas meta -->

  <!-- Etiquetas de Open Graph y redes sociales -->
  <meta property="og:title" content="Título de la página">
  <!-- otras etiquetas sociales -->

  <link rel="canonical" href="https://example.com/pagina.html">
  <!-- otras etiquetas link, salvo hojas de estilo e indicios de recursos -->

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
  Estas dos etiquetas deben aparecer lo antes posible dentro del <head>
  para garantizar un renderizado correcto del documento.
  Cualquier otro elemento del head debe ir *después* de ellas.
-->
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<!--
  Controla desde qué orígenes se pueden cargar los recursos.
  Colóquela lo antes posible en el <head>: la etiqueta solo
  se aplica a los recursos declarados después de ella.
-->
<meta http-equiv="Content-Security-Policy" content="default-src 'self'">

<!-- Nombre de la aplicación web (úsela solo si el sitio funciona como aplicación) -->
<meta name="application-name" content="Nombre de la aplicación">

<!-- Color de tema para Chrome, Firefox OS y Opera -->
<meta name="theme-color" content="#4285f4">

<!-- Un color de tema por esquema de color; el navegador elige el que corresponde -->
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0b0b0b" media="(prefers-color-scheme: dark)">

<!-- Indica los esquemas de color admitidos por la página (claro, oscuro o ambos) -->
<meta name="color-scheme" content="light dark">

<!-- Descripción breve del documento (máximo 150 caracteres) -->
<!-- Este contenido *puede* aparecer en los resultados de los buscadores. -->
<meta name="description" content="Una descripción de la página">

<!-- Controla el rastreo y la indexación por parte de los buscadores -->
<meta name="robots" content="index,follow"><!-- Todos los buscadores -->
<meta name="googlebot" content="index,follow"><!-- Solo Google -->

<!--
  Controla cuánto pueden mostrar los buscadores de la página.
  Estas directivas también determinan la elegibilidad para Google Discover
  y para las vistas previas enriquecidas: Discover exige una imagen grande.
-->
<meta name="robots" content="max-snippet:-1, max-image-preview:large, max-video-preview:-1">

<!-- Pide a Google que no muestre el cuadro de búsqueda de enlaces de sitio -->
<meta name="google" content="nositelinkssearchbox">

<!-- Pide a Google que no ofrezca traducción de este documento -->
<meta name="google" content="notranslate">

<!-- Verificación de la propiedad del sitio -->
<meta name="google-site-verification" content="token_de_verificacion"><!-- Google Search Console -->
<meta name="yandex-verification" content="token_de_verificacion"><!-- Yandex Webmasters -->
<meta name="msvalidate.01" content="token_de_verificacion"><!-- Bing Webmaster Center -->
<meta name="p:domain_verify" content="codigo_de_pinterest"><!-- Consola de Pinterest -->
<meta name="norton-safeweb-site-verification" content="codigo_norton"><!-- Norton Safe Web -->

<!-- Identifica el software con el que se generó el documento (WordPress, Dreamweaver, etc.) -->
<meta name="generator" content="programa">

<!-- Descripción breve del tema del documento -->
<meta name="subject" content="tema del documento">

<!-- Clasificación general por edad, según el contenido del documento -->
<meta name="rating" content="General">

<!-- Controla cómo se transmite la información del referente -->
<meta name="referrer" content="no-referrer">

<!-- Desactiva la detección y el formateo automáticos de números de teléfono -->
<meta name="format-detection" content="telephone=no">

<!-- Etiquetas geográficas -->
<meta name="ICBM" content="latitud, longitud"><!-- Coordenadas geográficas en grados decimales; p. ej. content="40.4168, -3.7038" -->
<meta name="geo.position" content="latitud;longitud"><!-- Coordenadas geográficas; latitud y longitud separadas por punto y coma -->
<meta name="geo.region" content="país[-región]"><!-- Código de país (ISO 3166-1) obligatorio, código de región (ISO 3166-2) opcional; p. ej. content="ES" / content="ES-MD" -->
<meta name="geo.placename" content="ciudad"><!-- p. ej. content="Madrid" -->

<!-- Web Monetization https://webmonetization.org/docs/getting-started -->
<meta name="monetization" content="$punterodepago.example">
```

**Nota:** las etiquetas geográficas **no** las usan directamente los navegadores. Están pensadas para buscadores, rastreadores y servicios de geolocalización, que las emplean para determinar la relevancia geográfica de una página. `ICBM` (llamada así por la convención militar de direcciones del mismo nombre) y `geo.position` expresan coordenadas en grados decimales; `ICBM` separa con coma y `geo.position` con punto y coma. `geo.region` identifica el país y, opcionalmente, la región mediante códigos ISO; `geo.placename` aporta un nombre de lugar legible.

- 📖 [Etiquetas meta que Google admite](https://developers.google.com/search/docs/crawling-indexing/special-tags?hl=es)
- 📖 [WHATWG Wiki: MetaExtensions](https://wiki.whatwg.org/wiki/MetaExtensions)
- 📖 [ICBM en Wikipedia](https://en.wikipedia.org/wiki/ICBM_address#Modern_use)
- 📖 [Geoetiquetado en Wikipedia](https://en.wikipedia.org/wiki/Geotagging#HTML_pages)

## Link

```html
<!-- Señala una hoja de estilos externa -->
<link rel="stylesheet" href="https://example.com/styles.css">

<!-- Evita los problemas de contenido duplicado -->
<link rel="canonical" href="https://example.com/articulo/?page=2">

<!-- Señala un manifiesto de aplicación web: la forma recomendada de declarar los metadatos de una PWA (nombre, iconos, theme_color, modo de visualización) -->
<link rel="manifest" href="manifest.json">

<!-- Remite a información sobre el autor o los autores del documento -->
<link rel="author" href="humans.txt">

<!-- Señala la declaración de derechos aplicable al contexto del enlace -->
<link rel="license" href="copyright.html">

<!-- Indica una versión del documento en otro idioma -->
<link rel="alternate" href="https://fr.example.com/" hreflang="fr">

<!-- Aporta información sobre un autor u otra persona.
     Lo usa RelMeAuth, una forma distribuida de verificación de identidad.
     Véase https://microformats.org/wiki/RelMeAuth -->
<link rel="me" href="https://google.com/profiles/thenextweb" type="text/html">
<link rel="me" href="mailto:nombre@example.com">
<link rel="me" href="sms:+34600000000">

<!-- Autorreferencia: útil cuando el documento es accesible desde varias direcciones -->
<link rel="self" type="application/atom+xml" href="https://example.com/atom.xml">

<!-- Documentos anterior y siguiente dentro de una serie -->
<link rel="prev" href="https://example.com/articulo/?page=1">
<link rel="next" href="https://example.com/articulo/?page=3">

<!-- Avisa a una URL cuando la enlaza desde su documento
     Más información en https://webmention.net -->
<link rel="webmention" href="https://example.com/webmention">

<!-- Permite publicar en su propio dominio desde un cliente Micropub
     Más información en https://indieweb.org/Micropub -->
<link rel="micropub" href="https://example.com/micropub">

<!-- Permite usar IndieAuth, una solución de identidad que le
     autentica mediante su nombre de dominio.
     Véase https://indieauth.net -->
<link rel="token_endpoint" href="https://example.com/token">
<link rel="authorization_endpoint" href="https://example.com/auth">

<!-- OpenSearch -->
<link rel="search" href="/open-search.xml" type="application/opensearchdescription+xml" title="Título de la búsqueda">

<!-- Fuentes -->
<link rel="alternate" href="https://feeds.feedburner.com/example" type="application/rss+xml" title="RSS">
<link rel="alternate" href="https://example.com/feed.atom" type="application/atom+xml" title="Atom 0.3">

<!-- Precarga, preconexión y prenavegación -->
<!-- Más información: https://css-tricks.com/prefetching-preloading-prebrowsing/ -->
<link rel="dns-prefetch" href="//example.com/">
<link rel="preconnect" href="https://www.example.com/">
<link rel="prefetch" href="https://www.example.com/">

<link rel="preload" href="imagen.png" as="image">

<!-- Sube o baja la prioridad de un recurso precargado -->
<link rel="preload" href="hero.avif" as="image" fetchpriority="high">

<!-- Precarga un módulo ES y todo su grafo de dependencias, sin ejecutarlo -->
<link rel="modulepreload" href="/js/app.js">
```

**Nota:** el [manifiesto de aplicación web](https://developer.mozilla.org/es/docs/Web/Progressive_web_apps/Manifest) (`manifest.json`) es la forma recomendada y multiplataforma de declarar las propiedades de una aplicación instalable — `name`, `icons`, `theme_color`, modo `display` — en un único archivo, en lugar de multiplicar etiquetas `<meta>` propias de cada plataforma.

- 📖 [Relaciones de enlace (IANA)](https://www.iana.org/assignments/link-relations/link-relations.xhtml)
- 📖 [Manifiesto de aplicación web (MDN)](https://developer.mozilla.org/es/docs/Web/Progressive_web_apps/Manifest)

## Scripts

```html
<!--
  Scripts: coloque las etiquetas <script> al final del <body> siempre que pueda.
  Estos atributos determinan el comportamiento de carga dentro del <head>:
-->

<!-- Bloquea el análisis del HTML y el renderizado hasta que el script se descarga y se ejecuta -->
<script src="script.js"></script>

<!-- El script se descarga en paralelo al análisis y se ejecuta en cuanto está disponible, antes de que el análisis termine -->
<script async src="script.js"></script>

<!-- El script se descarga en paralelo al análisis y se ejecuta cuando la página ha terminado de analizarse -->
<script defer src="script.js"></script>

<!-- async prevalece en los navegadores modernos; defer sirve de alternativa en los antiguos que no admiten async -->
<script async defer src="script.js"></script>

<!-- Script escrito dentro del propio documento -->
<script>
  // aquí van las funciones
</script>

<!-- Integridad de subrecursos (SRI): el atributo integrity comprueba que el recurso no se ha alterado por el camino -->
<script src="https://example.com/script.js" integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC"></script>
```

- 📖 [async frente a defer](https://www.growingwiththeweb.com/2014/02/async-vs-defer-attributes.html)
- 📖 [Integridad de subrecursos (MDN)](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Subresource_Integrity)

## Reglas de especulación

Las reglas de especulación le indican al navegador qué documentos es probable que abra el usuario a continuación, para que los precargue, o incluso los prerrenderice, antes del clic. Se declaran en el `<head>`, dentro de un bloque de script en JSON.

```html
<script type="speculationrules">
{
  "prerender": [
    {
      "where": {
        "and": [
          { "href_matches": "/*" },
          { "not": { "href_matches": "/cerrar-sesion" } },
          { "not": { "selector_matches": ".no-prerender" } },
          { "not": { "selector_matches": "[rel~=nofollow]" } }
        ]
      },
      "eagerness": "moderate"
    }
  ],
  "prefetch": [
    {
      "urls": ["pagina-2.html", "pagina-3.html"],
      "requires": ["anonymous-client-ip-when-cross-origin"],
      "referrer_policy": "no-referrer"
    }
  ]
}
</script>
```

`eagerness` admite `immediate`, `eager`, `moderate` y `conservative`, de más a menos especulativo. `moderate` se activa al pasar el cursor; `conservative`, al pulsar el botón.

Dos cosas que conviene saber antes de llevar esto a producción:

- **Una página prerrenderizada ejecuta su JavaScript.** La analítica, las llamadas publicitarias y las pruebas A/B pueden dispararse para una visita que nunca llegará a producirse. Condiciónelas a `document.prerendering` y al evento `prerenderingchange`.
- **Excluya todo lo que tenga efectos secundarios:** cerrar sesión, añadir al carrito, acciones de un solo clic. Para eso están las reglas `where` de arriba.

- 📖 [API Speculation Rules (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API)
- 📖 [Prerrenderizado de páginas en Chrome](https://developer.chrome.com/docs/web-platform/prerender-pages)

## Fragmentos de búsqueda y respuestas de IA

Lo que un buscador, o un motor de respuestas, puede reproducir de su página se controla mediante las directivas de fragmento. No existe una etiqueta dedicada.

```html
<!-- Ningún fragmento de texto para esta página -->
<meta name="robots" content="nosnippet">

<!-- Limita el fragmento a 160 caracteres; -1 significa sin límite -->
<meta name="robots" content="max-snippet:160">

<!-- Vista previa de imagen grande: imprescindible para ser elegible en Google Discover -->
<meta name="robots" content="max-image-preview:large">
```

Dentro del documento, `data-nosnippet` excluye un elemento concreto del fragmento:

```html
<p>Visible para todos. <span data-nosnippet>Nunca se cita en los resultados.</span></p>
```

**Ninguna etiqueta del `<head>` gobierna el entrenamiento de modelos ni las respuestas de las IA.** Esos controles están en el `robots.txt`, mediante tokens de agente como `Google-Extended`, `GPTBot`, `PerplexityBot` y `CCBot`, y mediante la propuesta Content Signals. Conviene recordar que `Google-Extended` afecta a Gemini y al anclaje de Vertex AI: no tiene ningún efecto sobre Google Search, ni sobre las AI Overviews, que dependen de Googlebot y de las directivas de fragmento anteriores.

- 📖 [Etiquetas y atributos que Google admite](https://developers.google.com/search/docs/crawling-indexing/special-tags?hl=es)
- 📖 [Google-Extended](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers?hl=es#google-extended)

## Iconos

```html
<!-- Para Internet Explorer 10 y anteriores -->
<!-- Coloque favicon.ico en la raíz; no hace falta ninguna etiqueta -->

<!-- El icono en la resolución más alta que necesite -->
<link rel="icon" sizes="192x192" href="/ruta/al/icono.png">

<!-- Icono táctil de Apple (reutiliza el icono de 192 px) -->
<link rel="apple-touch-icon" href="/ruta/al/apple-touch-icon.png">
```

- 📖 [Todo sobre los favicons y los iconos táctiles](https://bitsofco.de/all-about-favicons-and-touch-icons/)
- 📖 [Chuleta de favicons](https://github.com/audreyfeldroy/favicon-cheat-sheet)
- 📖 [Iconos y colores de navegador](https://web.dev/articles/icons-and-browser-colors)

## Social

### Open Graph

> El [protocolo Open Graph](https://ogp.me/) es el estándar de facto para controlar cómo aparece su contenido cuando se comparte. Creado en su día por Facebook, hoy lo utilizan la mayoría de las grandes plataformas: LinkedIn, X (como alternativa cuando faltan las etiquetas de Twitter Card), Discord, Slack, iMessage, Mastodon, Bluesky y WhatsApp.

```html
<meta property="og:url" content="https://example.com/pagina.html">
<meta property="og:type" content="website">
<meta property="og:title" content="Título del contenido">
<meta property="og:image" content="https://example.com/imagen.jpg">
<meta property="og:image:alt" content="Descripción de lo que muestra la imagen, no un pie de foto">
<meta property="og:description" content="Descripción aquí">
<meta property="og:site_name" content="Nombre del sitio">
<meta property="og:locale" content="es_ES">
<meta property="article:author" content="">
```

- 📖 [Protocolo Open Graph](https://ogp.me/)
- 🛠 Pruebe su página con el [depurador de compartidos de Facebook](https://developers.facebook.com/tools/debug/) o el [Post Inspector de LinkedIn](https://www.linkedin.com/post-inspector/)

### Schema.org

```html
<html lang="" itemscope itemtype="https://schema.org/Article">
    <head>
      <link rel="author" href="">
      <link rel="publisher" href="">
      <meta itemprop="name" content="Título del contenido">
      <meta itemprop="description" content="Descripción del contenido, menos de 200 caracteres">
      <meta itemprop="image" content="https://example.com/imagen.jpg">
```

**Nota:** estas etiquetas exigen que los atributos `itemscope` e `itemtype` estén en la etiqueta `<html>`.

- 📖 [Primeros pasos — schema.org](https://schema.org/docs/gs.html)
- 🛠 Pruebe su página con la [prueba de resultados enriquecidos](https://search.google.com/test/rich-results?hl=es)

### JSON-LD para Google

Este marcado ayuda a Google a generar un panel de grafo de conocimiento para su marca: el recuadro que aparece a la derecha de los resultados, normalmente en marcas ya establecidas.

```html
<script type="application/ld+json">
  {
    "@context": "http://schema.org",
    "@type": "Organization",
    "name": "sumarca.com",
    "url": "https://www.sumarca.com/",
    "logo": "https://www.sumarca.com/logo.png",
    "sameAs": [
      "https://www.facebook.com/sumarca",
      "https://twitter.com/sumarca",
      "https://es.pinterest.com/sumarca/",
      "https://www.instagram.com/sumarca/",
      "https://www.linkedin.com/company/sumarca"
    ]
  }
</script>
```

### Pinterest

Pinterest permite impedir que se guarden contenidos desde su sitio, [según su centro de ayuda](https://help.pinterest.com/es/business/article/prevent-saves-to-pinterest-from-your-site). El atributo `description` es opcional.

```html
<meta name="pinterest" content="nopin" description="Lo siento, desde este sitio no se puede guardar.">
```

### OEmbed

```html
<link rel="alternate" type="application/json+oembed"
  href="https://example.com/services/oembed?url=http%3A%2F%2Fexample.com%2Ffoo%2F&amp;format=json"
  title="Perfil oEmbed: JSON">
<link rel="alternate" type="text/xml+oembed"
  href="https://example.com/services/oembed?url=http%3A%2F%2Fexample.com%2Ffoo%2F&amp;format=xml"
  title="Perfil oEmbed: XML">
```

- 📖 [Formato oEmbed](https://oembed.com/)

### QQ/WeChat

Las páginas compartidas en QQ y WeChat se muestran como un mensaje con formato.

```html
<meta itemprop="name" content="título del contenido compartido">
<meta itemprop="image" content="http://imgcache.qq.com/qqshow/ac/v4/global/logo.png">
<meta name="description" itemprop="description" content="contenido compartido">
```

- 📖 [Documentación del formato](https://open.mobile.qq.com/api/mqq/index#api:setShareInfo)

### Dublin Core

[Dublin Core](https://www.dublincore.org/) es un vocabulario de metadatos normalizado como [ISO 15836](https://www.iso.org/standard/71339.html) y mantenido por la Dublin Core Metadata Initiative. Define quince elementos para describir un recurso y se usa ampliamente en bibliotecas digitales, repositorios institucionales, edición académica y portales públicos. Para emplearlo en HTML, declare el espacio de nombres DC y añada después los elementos que necesite como etiquetas `<meta>` con el prefijo `DC.`.

```html
<!-- Declaración del espacio de nombres Dublin Core -->
<link rel="schema.DC" href="https://purl.org/dc/elements/1.1/">

<meta name="DC.title" content="Título de la página">
<meta name="DC.creator" content="Nombre del autor">
<meta name="DC.subject" content="Palabras clave; temas">
<meta name="DC.description" content="Breve descripción del contenido de la página">
<meta name="DC.publisher" content="Nombre del editor">
<meta name="DC.contributor" content="Nombre del colaborador">
<meta name="DC.date" content="AAAA-MM-DD">
<meta name="DC.type" content="Text">
<meta name="DC.format" content="text/html">
<meta name="DC.identifier" content="https://example.com/pagina.html">
<meta name="DC.source" content="https://example.com/fuente-original">
<meta name="DC.language" content="es">
<meta name="DC.relation" content="https://example.com/recurso-relacionado">
<meta name="DC.coverage" content="Cobertura geográfica o temporal">
<meta name="DC.rights" content="Titular de los derechos">
```

- 📖 [Dublin Core Metadata Element Set](https://www.dublincore.org/specifications/dublin-core/dces/)
- 📖 [Usar Dublin Core en HTML](https://www.dublincore.org/specifications/dublin-core/dcq-html/)

### Fediverso

Algunos programas del fediverso, Mastodon entre ellos, permiten declarar su identificador en una etiqueta meta, que aparecerá en las vistas previas de sus páginas. Además de la etiqueta, hay que añadir su dominio a la lista de sitios autorizados: «Preferencias → Perfil público → Verificación → Atribución de autoría» en Mastodon.

```html
<meta name="fediverse:creator" content="@identificador@example.org">
```

## Navegadores y plataformas

### Apple iOS

```html
<!-- Banner Smart App Banner -->
<meta name="apple-itunes-app" content="app-id=APP_ID,affiliate-data=AFFILIATE_ID,app-argument=TEXTO">

<!-- Desactiva la detección y el formateo automáticos de números de teléfono -->
<meta name="format-detection" content="telephone=no">

<!-- Icono de lanzamiento (180 × 180 px o más) -->
<link rel="apple-touch-icon" href="/ruta/al/apple-touch-icon.png">

<!-- Imagen de la pantalla de inicio -->
<link rel="apple-touch-startup-image" href="/ruta/al/lanzamiento.png">

<!-- Título del icono de lanzamiento -->
<meta name="apple-mobile-web-app-title" content="Título de la aplicación">

<!-- Activa el modo autónomo, a pantalla completa -->
<meta name="mobile-web-app-capable" content="yes">

<!-- Aspecto de la barra de estado (sin efecto si el modo autónomo no está activado) -->
<meta name="apple-mobile-web-app-status-bar-style" content="black">

<!-- Adaptación a pantallas con muesca (iPhone X y posteriores); añada viewport-fit=cover a su etiqueta viewport existente -->
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">

<!-- Enlaces profundos a una aplicación de iOS -->
<meta name="apple-itunes-app" content="app-id=APP-ID, app-argument=http/url-ejemplo.com">
<link rel="alternate" href="ios-app://APP-ID/http/url-ejemplo.com">
```

- 📖 [Configuring Web Applications (Apple)](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html)

**Nota:** el título de la aplicación (`apple-mobile-web-app-title`), el modo de visualización y los iconos (`apple-touch-icon`) se configuran de forma más fiable y portable mediante el [manifiesto de aplicación web](https://developer.mozilla.org/es/docs/Web/Progressive_web_apps/Manifest) (`<link rel="manifest">`), que es el método recomendado para una PWA. Las etiquetas propias de Apple siguen siendo útiles como alternativa en versiones antiguas de iOS.

### Google Android

```html
<meta name="theme-color" content="#E64545">

<!-- Añadir a la pantalla de inicio -->
<meta name="mobile-web-app-capable" content="yes">
<!-- Más información: https://developer.chrome.com/multidevice/android/installtohomescreen -->

<!-- Enlaces profundos a una aplicación de Android -->
<meta name="google-play-app" content="app-id=nombre-del-paquete">
<link rel="alternate" href="android-app://nombre-del-paquete/http/url-ejemplo.com">
```

**Nota:** `theme-color` y el comportamiento de «añadir a la pantalla de inicio» se definen mejor mediante el [manifiesto de aplicación web](https://developer.mozilla.org/es/docs/Web/Progressive_web_apps/Manifest) (`<link rel="manifest">`). La etiqueta `theme-color` conserva su utilidad como alternativa en los navegadores que todavía no admiten la propiedad `theme_color` del manifiesto.

### Google Chrome

```html
<link rel="chrome-webstore-item" href="https://chrome.google.com/webstore/detail/APP_ID">

<!-- Desactiva la propuesta de traducción -->
<meta name="google" content="notranslate">
```

## Navegadores chinos

### Navegador 360

```html
<!-- Elige el orden de los motores de renderizado -->
<meta name="renderer" content="webkit|ie-comp|ie-stand">
```

### QQ Mobile Browser

```html
<!-- Bloquea la pantalla en la orientación indicada -->
<meta name="x5-orientation" content="landscape/portrait">

<!-- Muestra el documento a pantalla completa -->
<meta name="x5-fullscreen" content="true">

<!-- Muestra el documento en «modo aplicación»: pantalla completa, etc. -->
<meta name="x5-page-mode" content="app">
```

### UC Mobile Browser

```html
<!-- Bloquea la pantalla en la orientación indicada -->
<meta name="screen-orientation" content="landscape/portrait">

<!-- Muestra el documento a pantalla completa -->
<meta name="full-screen" content="yes">

<!-- UC muestra las imágenes incluso en «modo texto» -->
<meta name="imagemode" content="force">

<!-- Muestra el documento en «modo aplicación»: pantalla completa, gestos desactivados, etc. -->
<meta name="browsermode" content="application">

<!-- Desactiva el «modo nocturno» de UC para este documento -->
<meta name="nightmode" content="disable">

<!-- Simplifica el documento para reducir la transferencia de datos -->
<meta name="layoutmode" content="fitscreen">

<!-- Desactiva el aumento automático de la fuente en documentos con mucho texto -->
<meta name="wap-font-scale" content="no">
```

- 📖 [Documentación de UC Browser](https://www.uc.cn/download/UCBrowser_U3_API.doc)

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

<!-- Alternativa web -->
<meta property="al:web:url" content="https://applinks.org/documentation">
```

- 📖 [App Links](https://developers.facebook.com/docs/applinks)

## Obsoleto

Para las etiquetas y los elementos que formaron parte de esta guía y ya no se admiten —compatibilidad con Internet Explorer, pestañas ancladas de Safari, la etiqueta `view-transition`, verificación de Alexa, etc.— consulte [DEPRECATED.md](./DEPRECATED.md).

## Otros recursos

- 📖 [HTML5 Boilerplate: el HTML](https://github.com/h5bp/html5-boilerplate/blob/main/docs/html.md)
- 📖 [HTML5 Boilerplate: ampliar y personalizar](https://github.com/h5bp/html5-boilerplate/blob/main/docs/extend.md)

## Proyectos relacionados

- [head-it](https://github.com/hemanth/head-it) — interfaz de línea de comandos para los fragmentos de `<head>`
- [Sublime Text HTML Head Snippets](https://github.com/marcobiedermann/sublime-head-snippets) — fragmentos de `<head>` para Sublime Text
- [vue-head](https://github.com/ktquez/vue-head) — gestión de los metadatos del `<head>` en Vue.js

## 🌐 Traducciones

- [English](./README.md)
- [Français](./README.fr.md)

## 🤝 Contribuir

**Abra una incidencia o una solicitud de fusión para proponer una adición o una corrección.**

Convenciones a respetar:

- Modifique solo una etiqueta, o un conjunto coherente de etiquetas, cada vez
- Use comillas dobles en los atributos
- Sin barra final en los elementos de cierre automático: la especificación HTML5 la considera opcional
- Incluya un enlace a la documentación que respalde su cambio
- Si una etiqueta queda obsoleta o es sustituida, muévala a [DEPRECATED.md](./DEPRECATED.md) en lugar de borrarla, e indique su reemplazo

## 👤 Autor

**David Corroy** — consultor SEO, Francia.

Mantengo esta guía porque el `<head>` es donde se decide la visibilidad de una página, y la mayoría de las referencias sobre el tema llevan años sin actualizarse.

- 🌐 Sitio web: [david-corroy.com](https://david-corroy.com)
- 🦊 GitLab: [@david-corroy](https://gitlab.com/david-corroy)
- 🐙 GitHub: [@david-corroy](https://github.com/david-corroy)

## ⭐ Apoyar

Si esta guía le ha ahorrado tiempo:

- ⭐ Déjele una estrella, en [GitLab](https://gitlab.com/david-corroy/head) o en [GitHub](https://github.com/david-corroy/HEAD)
- 🗣 Abra una incidencia cuando encuentre una etiqueta que falte, o una que ya no haga nada
- 🔗 Enlace esta guía en lugar de copiarla, para que sus lectores tengan siempre la versión corregida

## 📝 Licencia

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/deed.es)

Esta obra está dedicada al dominio público bajo [CC0 1.0 Universal](./LICENSE). Puede copiarla, modificarla y distribuirla, incluso con fines comerciales, sin pedir permiso.
