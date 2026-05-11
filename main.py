# -*- coding: utf-8 -*-

"""
Phase 1 test app.

This APK only tests that the English UI appears correctly on Android.
PDF selection and text extraction will be added in Phase 2 after this test works.
"""

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


def make_center_label(text, font_size="16sp", height=None):
    label = Label(
        text=text,
        font_size=font_size,
        halign="center",
        valign="middle",
    )

    def update_text_size(instance, size):
        instance.text_size = size

    label.bind(size=update_text_size)

    if height is not None:
        label.size_hint_y = None
        label.height = dp(height)

    return label


def make_button(text):
    return Button(
        text=text,
        font_size="18sp",
        size_hint_y=None,
        height=dp(55),
    )


class PdfToTxtPhase1App(App):
    def build(self):
        self.title = "PDF to TXT"

        root = BoxLayout(
            orientation="vertical",
            padding=dp(16),
            spacing=dp(12),
        )

        root.add_widget(
            make_center_label(
                "PDF to Arabic TXT",
                font_size="24sp",
                height=dp(60),
            )
        )

        root.add_widget(
            make_center_label(
                "Phase 1 test app.\n"
                "The English interface should appear normally.\n\n"
                "No PDF extraction is included yet.",
                font_size="16sp",
            )
        )

        root.add_widget(make_button("Open Storage"))
        root.add_widget(make_button("Extract Selected PDFs"))
        root.add_widget(make_button("Clear Selection"))

        root.add_widget(
            make_center_label(
                "Ready.",
                font_size="15sp",
                height=dp(45),
            )
        )

        return root


if __name__ == "__main__":
    PdfToTxtPhase1App().run()
