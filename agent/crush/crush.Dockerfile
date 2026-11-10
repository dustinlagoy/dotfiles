# FROM golang:trixie AS build
# ADD https://github.com/dustinlagoy/crush/info/refs?service=git-upload-pack version.json
# RUN git clone --branch test-new-gpt https://github.com/dustinlagoy/crush.git /crush
# WORKDIR /crush
# RUN go build


FROM debian:trixie
RUN apt-get update && apt-get install --yes --no-install-recommends curl ca-certificates git
ADD https://astral.sh/uv/install.sh uv.sh
RUN sh ./uv.sh && rm ./uv.sh 
ENV PATH="/root/.local/bin:$PATH"
RUN uv tool install markitdown-mcp
ADD https://github.com/dustinlagoy/dotfiles.git /root/dotfiles/
WORKDIR /root/dotfiles/agent
RUN ./install.sh
WORKDIR /work
# TODO add some tools for crush
# COPY --from=build --chmod=755 /crush/crush /usr/local/bin/crush
RUN curl -L https://github.com/charmbracelet/crush/releases/download/v0.79.1/crush_0.79.1_Linux_x86_64.tar.gz \
        | tar -xzO crush_0.79.1_Linux_x86_64/crush > /usr/local/bin/crush && \
    chmod 755 /usr/local/bin/crush
CMD ["/usr/local/bin/crush"]
