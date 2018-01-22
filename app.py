import json
import pdfkit

from jinja2 import Template, Environment, FileSystemLoader


def app():
    print('*********************** app started ***********************')
    data = json.load(open('input/data.json'))

    # itterate over input data
    for item in data:

        print(item)
        print(item['url_name'])

        # context data for template

        # set options for print
        options = {
            'page-size': 'A4',
            'margin-top': '0',
            'margin-right': '0',
            'margin-bottom': '0',
            'margin-left': '0',
            'disable-smart-shrinking': None,
            'zoom': 3.1
        }

        # generate file and save it to output folder
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('template.html')
        output_from_parsed_template = template.render(email=item['email'], name=item['name'], url_name=item['url_name'])

        save_file_name = 'output/' + item['name'] + '.pdf'

        pdfkit.from_string(output_from_parsed_template, save_file_name, options=options)

app()

# TODO: sys args

# if __name__ == '__main__':
#     if len(sys.argv) > 1 and sys.argv[1] == "build":
#         freezer.run(debug=True)
#     elif len(sys.argv) > 1 and sys.argv[1] == "filldb":
#         filldb()
#         createEshopOrder()
#     else:
#         manager.run(host='0.0.0.0')
