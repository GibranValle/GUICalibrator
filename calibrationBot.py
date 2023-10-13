def main():
    from util.CustomExceptions import AbortionRequestError

    app = gui.App()

    try:
        app.mainloop()  # type: ignore
    except AbortionRequestError:
        app.generic.abort_requested()


if __name__ == "__main__":
    import classes.GUI as gui

    main()
