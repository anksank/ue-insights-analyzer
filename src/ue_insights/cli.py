import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trace", required=True)
    parser.add_argument("--profile", default="low_end")
    parser.add_argument("--frame-count", type=int, required=True)
    parser.add_argument("--with-llm", action="store_true")
    args = parser.parse_args()
