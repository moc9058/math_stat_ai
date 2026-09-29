"""Check the project API key without printing it."""

from pathlib import Path

from openai import OpenAI


def main() -> None:
    env_path = Path(__file__).resolve().parents[3] / ".env"
    key = next(
        line.split("=", 1)[1].strip()
        for line in env_path.read_text(encoding="utf-8").splitlines()
        if line.startswith("OPENAI_API_KEY=")
    )
    try:
        response = OpenAI(api_key=key, timeout=30).responses.create(
            model="gpt-6-luna",
            reasoning={"effort": "low"},
            input="Reply with exactly OK.",
        )
        print("response=", response.output_text.strip())
        print("input_tokens=", response.usage.input_tokens)
        print("output_tokens=", response.usage.output_tokens)
    except Exception as exc:
        print("api_error_type=", type(exc).__name__)
        raise SystemExit(1) from None


if __name__ == "__main__":
    main()
