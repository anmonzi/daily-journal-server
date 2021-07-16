from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from entries import get_all_entries
# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.


class HandleRequests(BaseHTTPRequestHandler):
    # This is a Docstring it should be at the beginning of all classes and functions
    # It gives a description of the class or function
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def parse_url(self, path):
        """Parse url string
        """
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple

    # Here's a class function

    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                        'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                        'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        """Handles GET requests to the server
        """
        # Set the response code to 'Ok'
        self._set_headers(200)
        response = {}  # Default response

        # Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)

        if resource == "entries":
            if id is not None:
                pass
                # response = f"{get_single_animal(id)}"
            else:
                response = f"{get_all_entries()}"

        # This weird code sends a response back to the client
        self.wfile.write(response.encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.

    # def do_POST(self):
    #     """Handles POST requests to the server
    #     """
    #     # Set response code to 'Created'
    #     self._set_headers(201)

    #     content_len = int(self.headers.get('content-length', 0))
    #     post_body = self.rfile.read(content_len)

    #     # Convert JSON string to a Python dictionary
    #     post_body = json.loads(post_body)

    #     # Parse the URL
    #     (resource, id) = self.parse_url(self.path)

    #     # Initializations of new data
    #     # was new_animal = None
    #     # Using response to keep code DRY "don't repeat yourself"
    #     response = None

    #     # Add a new animal or other new data to the list.
    #     if resource == "animals":
    #         response = create_animal(post_body)
    #     if resource == "locations":
    #         response = create_location(post_body)
    #     if resource == "employees":
    #         response = create_employee(post_body)
    #     if resource == "customers":
    #         response = create_customer(post_body)

    #     self.wfile.write(f"{response}".encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any PUT request.

    # def do_PUT(self):
    #     """Handles PUT requests to the server
    #     """
    #     self._set_headers(204)
    #     content_len = int(self.headers.get('content-length', 0))
    #     post_body = self.rfile.read(content_len)
    #     post_body = json.loads(post_body)

    #     # Pars the URL
    #     (resource, id) = self.parse_url(self.path)

    #     # Edit a single animal or other dictionary from the list
    #     if resource == "animals":
    #         update_animal(id, post_body)
    #     elif resource == "employees":
    #         update_employee(id, post_body)
    #     elif resource == "customers":
    #         update_customer(id, post_body)
    #     elif resource == "locations":
    #         update_location(id, post_body)

    #     # Encode the new animal and send in response
    #     self.wfile.write("".encode())


    # def do_DELETE(self):
    #     """Handles DELETE requests to the server
    #     """
    #     # Set a 204 response code
    #     self._set_headers(204)

    #     # Parse the URL
    #     (resource, id) = self.parse_url(self.path)

    #     # Delete a single animal/ or dictionary from the list by id
    #     if resource == "animals":
    #         delete_animal(id)
    #     elif resource == "locations":
    #         delete_location(id)
    #     elif resource == "employees":
    #         delete_employee(id)
    #     elif resource == "customers":
    #         delete_customer(id)

    #     # Encode the new animal and send in response
    #     self.wfile.write("".encode())


# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()