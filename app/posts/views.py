from flask import render_template, request, redirect, url_for, flash
from app import db
from .models import Post
from .forms import PostForm
from . import post_bp

@post_bp.route("/", methods=["GET"])
def all_posts():
    posts = Post.query.order_by(Post.posted.desc()).all()
    return render_template("all_posts.html", posts=posts)

@post_bp.route("/create", methods=["GET", "POST"])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            category=form.category.data,
            is_active=form.is_active.data,
            author=form.author.data
        )
        db.session.add(post)
        db.session.commit()
        flash("Post added successfully!", "success")
        return redirect(url_for("posts.all_posts"))
    return render_template("add_post.html", form=form)

@post_bp.route("/<int:id>", methods=["GET"])
def detail_post(id):
    post = Post.query.get_or_404(id)
    return render_template("detail_post.html", post=post)

@post_bp.route("/<int:id>/update", methods=["GET", "POST"])
def update_post(id):
    post = Post.query.get_or_404(id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        form.populate_obj(post)
        db.session.commit()
        flash("Post updated successfully!", "success")
        return redirect(url_for("posts.detail_post", id=post.id))
    return render_template("add_post.html", form=form)

@post_bp.route("/<int:id>/delete", methods=["POST"])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted successfully!", "info")
    return redirect(url_for("posts.all_posts"))
