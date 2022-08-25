import webview
import os


class Api:
    def destroy(self):
        print('Destroying window..')
        window.destroy()
        print('Destroyed!')

    def test(self):
        print('Test')


    def textureselect(self):
        file_types = ('Image Files (*.png)', 'All files (*.*)')
        result = window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=True, file_types=file_types)
        print(result)



    def folderselect(self):
        result = window.create_file_dialog(webview.FOLDER_DIALOG, allow_multiple=False)
        path = result
        print(path)
        file = path[0] + '\pack.mcmeta'
        if os.path.exists(file):
            print('Valid pack')
            window.evaluate_js(
                r"""
                showValidPackButton()
                """
            )
        else:
            print('Invalid pack')
            print('Displaying error')
            window.evaluate_js(
                r"""
                alert('This is not a valid resource pack');
                """
            )
        showpathinhtml = window.evaluate_js(
            r"""
            showResponse({message: ${path}})
            """
        )


    def showResponse(self):
        window.evaluate_js(
            r"""
            showResponse({message: path})
            """
        )


if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Resource', 'assets/main.html', js_api=api, min_size=(300, 100))
webview.start(debug=True)