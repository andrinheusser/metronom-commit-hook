#metronom-commit-hook

A git post-commit hook for adding worklogs to metronom via commit message

## Setup

Run `python setup.py`

#### metronom.apikey

Your Metronom API Key

#### metronom.job

The Job/Project ID of the project you are working on.

## Usage

The commit message is parsed, looking for this pattern: &lt;worklog&gt;#&lt;hours&gt;#&lt;activity&gt;

### Examples

git commit -m "a meaningful commit message/worklog. #1.2#backend"

### Available Activities

* dokumentation
* frontend
* suchmaschienenoptimierung
* verschiedenes
* fehlerbehebung
* seo
* testen
* backend
* mobile
* datenhandling
* coaching
* code review
