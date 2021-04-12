from flask import Blueprint, render_template, request, flash, redirect, url_for
from .hitungPPh21_OK import hitung

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        status = request.form.get("status")
        jumlah_tanggungan = request.form.get("jumlah_tanggungan")
        gaji = request.form.get("gaji")

        validate_status = ["K", "TK", "k", "tk"]

        if len(name) < 4:
            flash("nama terlalu pendek, isi minimal 4 karakter", category="error")
            return redirect(url_for("views.home"))
        elif status not in validate_status:
            flash("field status isi dengan 'K' atau 'TK'", category="error")
            return redirect(url_for("views.home"))
        elif int(jumlah_tanggungan) > 3:
            flash(
                "field jumlah tanggungan tidak boleh kosong dan tidak boleh lebih dari 3",
                category="error",
            )
            return redirect(url_for("views.home"))
        elif gaji == "":
            flash("field gaji harap di isi", category="error")
            return redirect(url_for("views.home"))
        elif gaji.isalpha():
            flash("field gaji harap di isi dengan angka", category="error")
            return redirect(url_for("views.home"))
        else:
            hasil = hitung(name, status, jumlah_tanggungan, gaji)
          
            return render_template("hasil.html", hasil=hasil)
    else:
        return render_template("input.html")
