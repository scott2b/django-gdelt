## Attribution

This package makes uses of resources from the GDELT project. It is the user's
responsibility to use this package within the (very liberal) parameter of
GDELT's terms of use (https://www.gdeltproject.org/about.html#termsofuse) which
are cited verbatim here (Apr 19, 2018):

### Using GDELT

The GDELT Project is an open platform for research and analysis of global society and thus all datasets released by the GDELT Project are available for unlimited and unrestricted use for any academic, commercial, or governmental use of any kind without fee.

### Redistributing GDELT

You may redistribute, rehost, republish, and mirror any of the GDELT datasets in any form. However, any use or redistribution of the data must include a citation to the GDELT Project and a link to this website (https://www.gdeltproject.org/).

For more information, see the GDELT website: https://www.gdeltproject.org/

## Installation

Add to settings.py:

```
INSTALLED_APPLICATIONS = (
    ...
    'djdelt',
    ...
)
```

## Usage

 To load category patterns used for theme and event matching:

    `./manage.py load_categories`

## Gdelt

Codebooks:
https://blog.gdeltproject.org/gdelt-2-0-our-global-world-in-realtime/
