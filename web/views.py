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
        jika_float = None
        try:
            jika_float = type(float(name))
        except:
            jika_float = ""

        if jika_float == float:
            flash("field nama tidak boleh angka", category="error")
            return redirect(url_for("views.home")) 
        elif len(name) < 4:
            flash("nama terlalu pendek, isi minimal 4 karakter", category="error")
            return redirect(url_for("views.home"))
        elif status not in validate_status:
            flash("field status isi dengan 'K' atau 'TK'", category="error")
            return redirect(url_for("views.home"))
        elif jumlah_tanggungan == "":
            flash("field jumlah tanggungan harap di isi",category="error")
            return redirect(url_for("views.home"))
        elif not jumlah_tanggungan.isnumeric() or int(jumlah_tanggungan) > 3:
            flash(
                "field jumlah tanggungan harap di isi dengan angka dan tidak boleh lebih dari 3",
                category="error",
            )
            return redirect(url_for("views.home"))
        elif gaji == "":
            flash("field gaji harap di isi", category="error")
            return redirect(url_for("views.home"))
        elif not gaji.isnumeric():
            flash("field gaji harap di isi dengan angka tanpa karakter lain", category="error")
            return redirect(url_for("views.home"))
        else:
            hasil = hitung(name, status, jumlah_tanggungan, gaji)
          
            return render_template("hasil.html", hasil=hasil)
    else:
        return render_template("input.html")
