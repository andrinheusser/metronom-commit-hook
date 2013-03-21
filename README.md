#metronom-commit-hook

A git post-commit hook for adding worklogs to metronom via commit message

## Setup

Copy this file to `.git/hooks/post-commit`

### Configuration

Use `git config` to configure the script

    git config metronom.apikey <APIKEY>
    git config metronom.job <jobid>

#### metronom.apikey

Your Metronom API Key

#### metronom.job

The Job/Project ID of the project you are working on.

## Usage

The commit message is parsed, looking for this pattern: #<hours>#<activity>

### Examples

git commit -m "Nubbel. #1.2#backend"

### Available Activities

*dokumentation
*frontend
*suchmaschienenoptimierung
*verschiedenes
*fehlerbehebung
*seo
*testen
*backend
*mobile
*datenhandling
*coaching
*code review
