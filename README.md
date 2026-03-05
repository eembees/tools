# tools.mags.nu

Assorted useful tools, hosted at [tools.mags.nu](https://tools.mags.nu).

Inspired by [simonw/tools](https://github.com/simonw/tools).

## Adding a tool

1. Create a self-contained HTML file at the repo root, e.g. `my-tool.html`
2. Add Jekyll front matter at the top so it appears in the index:
   ```html
   ---
   title: My Tool
   description: What it does
   ---
   <!DOCTYPE html>
   ...
   ```
3. Optionally include the shared footer before `</body>`:
   ```html
   <script src="/footer.js"></script>
   ```
4. Commit and push — GitHub Actions will deploy automatically.

## Local development

```bash
gem install bundler jekyll
jekyll serve
```

Then open http://localhost:4000.
