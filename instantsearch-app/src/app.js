const { algoliasearch, instantsearch } = window;

const searchClient = algoliasearch('UQYBDBYQUQ', '933e2673286ff2fac8b40120506d17bc');

const search = instantsearch({
  indexName: 'movies_index',
  searchClient,
  future: { preserveSharedStateOnUnmount: true },
  
});


search.addWidgets([
  instantsearch.widgets.searchBox({
    container: '#searchbox',
  }),
  instantsearch.widgets.hits({
    container: '#hits',
    templates: {
      item: (hit, { html, components }) => html`
<article>
  <div>
    <h1>${components.Highlight({hit, attribute: "keywords.0"})}</h1>
    <p>${components.Highlight({hit, attribute: "keywords.1"})}</p>
    <p>${components.Highlight({hit, attribute: "keywords.2"})}</p>
  </div>
</article>
`,
    },
  }),
  instantsearch.widgets.configure({
    hitsPerPage: 8,
  }),
  instantsearch.widgets.pagination({
    container: '#pagination',
  }),
]);

search.start();

