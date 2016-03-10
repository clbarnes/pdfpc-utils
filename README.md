# pdfpc-utils
Utilities for LaTeX Beamer presentations and pdfpc

Beamer presentations can have inline \notes{} tags; pdfpc uses an output file to hold the notes which are displayed while the presentation is run.

## `make_nodes.py`
`make_notes.py` extracts all of the inline notes into a `.pdfpc` file. Note - it'll break if there are any `}` characters in the text of the notes.

__Usage__: `python3 make_notes.py <presentation name>` (<presentation name> can be with or without the `.tex` extension)

## `add_slide.py`
`add_slide.py` addresses the fact that if a new slide is added to the presentation, there will be a frame shift in the pdfpc notes. Slides can be added manually.

__Usage__: `python3 add_slide.py <notes file> <slide index>`
