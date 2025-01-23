from locust import task, run_single_user
from locust import FastHttpUser

class Browse(FastHttpUser):
    host = "http://localhost:5000"
    default_headers = {
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "DNT": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
        "Upgrade-Insecure-Requests": "1",
    }

    @task
    def optimized_browse(self):
        with self.client.get(
            "/browse",
            headers=self.default_headers,
            catch_response=True
        ) as response:
            # Only process further if the response is successful
            if response.status_code == 200:
                # Simulate lightweight processing of response content
                if "products" not in response.text:
                    response.failure("Product details missing in the response.")
            else:
                response.failure(f"Unexpected status code: {response.status_code}")

# Corrected the name check to _name_ == "_main_"
if __name__ == "_main_":
    run_single_user(Browse)