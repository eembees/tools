/**
 * Shared footer for tools.mags.nu
 * Include before </body> in any tool page:
 *   <script src="/footer.js"></script>
 */
(function () {
  const path = window.location.pathname;
  const filename = path.split('/').pop() || 'index.html';
  const githubBase = 'https://github.com/eembees/tools/blob/main/';

  const footer = document.createElement('footer');
  footer.style.cssText = [
    'margin-top: 3rem',
    'padding: 1rem 0',
    'border-top: 1px solid #e1e4e8',
    'font-size: 0.85rem',
    'color: #586069',
    'font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif',
  ].join(';');

  const links = [
    { href: '/', text: 'Home' },
    { href: githubBase + filename, text: 'View source' },
    { href: 'https://github.com/eembees/tools', text: 'GitHub' },
  ];

  footer.innerHTML = links
    .map(
      (l) =>
        `<a href="${l.href}" style="color:#0366d6;text-decoration:none;margin-right:1rem">${l.text}</a>`
    )
    .join('');

  document.body.appendChild(footer);
})();
