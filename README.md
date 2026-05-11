# PDF to Arabic TXT — Phase 1

This repository builds a small Android APK using **Kivy + Buildozer + GitHub Actions**.

## What this Phase 1 APK does

It only tests that the English interface appears correctly on your Android phone.

It shows:

```text
PDF to Arabic TXT
Open Storage
Extract Selected PDFs
Clear Selection
Ready.
```

PDF selection and text extraction are not included yet.

## How to use on GitHub

1. Create a new GitHub repository.
2. Upload all files and folders from this project.
3. Go to the **Actions** tab.
4. Open **Build Android APK**.
5. Click **Run workflow**.
6. Wait until the build finishes.
7. Open the finished workflow run.
8. Download the APK from **Artifacts**.

## Next step

After Phase 1 works, we will add:

- Multi-PDF selection
- Storage browser
- Arabic TXT extraction using `pypdf`
- Output folder in `Download/PDF_TXT_Output`
