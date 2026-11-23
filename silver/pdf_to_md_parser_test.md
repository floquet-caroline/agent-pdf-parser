# PDF to Markdown Parser Test

*A compact text-only sample containing headings, emphasis, lists, a table, and special characters.*

## 1. Overview

This document is a small **synthetic test fixture** for evaluating how a PDF extraction pipeline preserves document structure. It intentionally combines several common formatting features in a short, readable layout.

A good parser should retain the distinction between **bold text**, *italic text*, _underlined text_, and ordinary text. It should also recognize headings and avoid merging unrelated paragraphs.

## 2. Unordered and Ordered Lists

The following list contains three independent items:

- Extract the text in its natural reading order.
- Preserve meaningful paragraph and heading boundaries.
- Represent tabular data without mixing adjacent cells.

A simple processing sequence:

1. Load the source PDF.
2. Extract text and layout information.
3. Convert detected structures into Markdown.
4. Review the output for missing or reordered content.

## 3. Table of Sample Data

The table below includes a header row, numeric values, and a final summary row.

<table>
  <thead>
    <tr>
      <th>Module</th>
      <th>Pages</th>
      <th>Status</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Text extraction</td>
      <td>2</td>
      <td>Complete</td>
      <td>98%</td>
    </tr>
    <tr>
      <td>Layout analysis</td>
      <td>3</td>
      <td>In review</td>
      <td>87%</td>
    </tr>
    <tr>
      <td>Markdown export</td>
      <td>1</td>
      <td>Pending</td>
      <td>—</td>
    </tr>
    <tr>
      <td>Total</td>
      <td>6</td>
      <td>3 modules</td>
      <td>92.5%</td>
    </tr>
  </tbody>
</table>

## 4. Quotation and Inline Details

> “The purpose of a test document is not to be realistic in every detail, but to make important behaviors easy to observe.”

Inline tokens: `parser_version = 1.4.2; confidence = 0.975; file_name = sample_input.pdf`.

---

PDF-to-Markdown test fixture
Page 1


# 5. Notes for Validation

Check whether the exported Markdown includes sensible heading levels, list markers, table separators, and paragraph breaks. The em dash (—), curly quotation marks (“ ”), and percentage sign (%) are included as additional character-level checks.

*End of sample. No images, diagrams, or embedded screenshots are present in this file.*

---

PDF-to-Markdown test fixture                                                                 Page 2
