playlist = {'title' : 'patagonia bus', 
            'author' : 'Norberto Sánchez-Dichi',
            'songs' : [
                {'title': 'song1',
                 'artist': ['blue'],
                 'duration' : 2.5
                },
                {'title': 'song2',
                 'artist': ['kitty', 'djcat'],
                 'duration' : 5.25
                },
                {'title': 'woofwoof',
                 'artist': ['Courage'],
                 'duration' : 2.0
                }
            ]
}
print(f'{playlist =}')

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']
    
print(f'{total_length =}')