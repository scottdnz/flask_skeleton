#!/usr/bin/env python


""" Executes Flask project. """


from flask_skeleton.config import app


# Remove the following lines in production.
try:
    import uwsgi

    @app.route("/_reload")
    def _reload():
        """Reloader. """
        return "Done"
except Exception as exc:
    print("uWSGI not detected")
    

if __name__ == "__main__":
    app.run("0.0.0.0", port=9000, debug=True)

