from dataclasses import dataclass

@dataclass
class Request:
    method: str
    path: str
    proto: str
    headers: dict[str, str]
    body: str

    @classmethod
    def from_str(cls, v: str) -> "Request":
        lines = v.splitlines()
        if not lines:
            raise ValueError("Empty request")

        request_line = lines[0].strip()
        parts = request_line.split()
        if len(parts) != 3:
            raise ValueError("Invalid request line")
        method, path, proto = parts

        # Headers
        headers = {}
        i = 1
        while i < len(lines) and lines[i].strip():
            header_line = lines[i].strip()
            if ":" not in header_line:
                raise ValueError("Invalid header")
            key, value = header_line.split(":", 1)
            headers[key.strip()] = value.strip()
            i += 1

        if i < len(lines) and not lines[i].strip():
            i += 1

        # Body
        body = "\n".join(lines[i:]) if i < len(lines) else ""

        return cls(method, path, proto, headers, body)

    def to_str(self) -> str:
        request_line = f"{self.method} {self.path} {self.proto}"
        headers_str = "\n".join(f"{key}: {value}" for key, value in self.headers.items())
        return f"{request_line}\n{headers_str}\n\n{self.body}"
