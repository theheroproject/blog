from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for, session

blog_abtest = Blueprint('blog', __name__)


@blog_abtest.route('/test')
def test():
    return render_template('blog_A.html')
