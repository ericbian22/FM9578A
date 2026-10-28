# Verification record

- Source inventory: 11 PDFs, 261 physical pages; all page ranges mapped in downloads/source-coverage.json. Repeated slide builds consolidated.
- Suggested exercises: Q1–20, 97 subparts retained. Brownian supplement: cases (a)–(i). Lecture 7: 1/4 grouped, 2, 3, 5 and 6 retained.
- Independent mathematical review found two wording issues: finite-horizon correlation versus local correlation, and local/Euler labels on Q20 moments. Both corrected. No numerical answer errors found in the 20 exercises or nine dependence cases.
- Numerical tests: European parity, non-dividend American call equality, American put dominance, early exercise, FX/futures growth, strategy payoffs, invalid-input handling, seeded Brownian paths, rho=±1.
- Browser checks: 9 lectures, 20 question panels, 97 subparts, 9 supplement cases; every lecture and sheet math expression rendered; zero KaTeX errors; search, progress persistence, solution expansion and all three tools exercised.
- Responsive widths: 1440, 390 and 320 pixels; no page-level horizontal overflow.
- PDF: exactly two US Letter pages, 612 × 792 points. Both rendered and visually inspected after final changes. Printed columns remain within page bounds, with no horizontal overflow. Last text baseline approximately 744 and 762 points from page top.
- Static publish artifact includes only index, formula sheet, assets and downloads.
- Known source limitation: L2 references a margin workbook not supplied.
- Source correction: L7 p13 root call value .9334 conflicts with given parameters; corrected to .9497 as in L6.
- Formula sheet is a condensed selected reference, not a claim to include every website example or complete solution.
- Handwriting edition: locally embedded Kalam regular/bold applied to text and mathematical lettering; both pages rendered and visually checked. Browser checks pass with column bottoms at approximately 1011 and 1017 CSS pixels within 1056-pixel pages. PDF text ends at approximately 750 and 755 points within 792-point US Letter pages. Content unchanged.
- GitHub Actions run 40628605181 succeeded. Live website returned HTTP 200 with 9 lectures, 97 exercise subparts and zero math-render errors. The live two-page PDF returned HTTP 200 and matched the inspected local file byte-for-byte (SHA-256 376a26d86fac8d9d09c489e7a987a644d4a26d5d304265f0039b0afa809ca246).
