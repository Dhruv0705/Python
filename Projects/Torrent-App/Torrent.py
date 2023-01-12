from torrentp import TorrentDownloader
torrent_file = TorrentDownloader("magnet:...", '.')
torrent_file.start_download()