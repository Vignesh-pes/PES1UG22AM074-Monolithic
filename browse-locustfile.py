from locust import task, run_single_user, HttpUser

class BrowseUser(HttpUser):
    host = "http://localhost:5000"  # Ensure this matches your running server's host

    # Consolidated default headers
    default_headers = {
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "DNT": "1",
        "Sec-GPC": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
        "Upgrade-Insecure-Requests": "1",
    }

    @task
    def browse_page(self):
        """Simulate browsing the products page."""
        with self.client.get(
            "/browse",
            headers=self.default_headers,
            catch_response=True,
        ) as response:
            # Validate response status and content
            if response.status_code == 200 and "products" in response.text:
                response.success()
            else:
                response.failure(f"Failed to load /browse. Status: {response.status_code}")

if __name__ == "_main_":
    run_single_user(BrowseUser)