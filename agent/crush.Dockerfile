FROM golang:trixie AS build
ADD https://github.com/dustinlagoy/crush/info/refs?service=git-upload-pack version.json
RUN git clone --branch custom-system-prompt https://github.com/dustinlagoy/crush.git /crush
WORKDIR /crush
RUN go build

FROM debian:trixie
RUN apt-get update && apt-get install --yes --no-install-recommends curl ca-certificates
ADD https://astral.sh/uv/install.sh uv.sh
RUN sh ./uv.sh && rm ./uv.sh 
ENV PATH="/root/.local/bin:$PATH"
RUN uv tool install markitdown-mcp
ADD https://github.com/dustinlagoy/dotfiles.git /root/dotfiles/
WORKDIR /root/dotfiles/agent
RUN ./install.sh
WORKDIR /work
# TODO add some tools for crush
COPY --from=build --chmod=755 /crush/crush /
CMD ["/crush"]
