default persistent.choosen_language = False

init -2 python:
    from collections import deque

    renpy.music.register_channel("ambience", "sfx", loop=True, tight=True)
    renpy.music.register_channel("ambfx", "sfx", loop=False, tight=True, buffer_queue=True)
    store._last_say_ended = -1.0

    channel_volumes = {}

    menu_duck_channels = ["music", "ambience", "ambfx"]
    
    def _any_char_cb(event, interact, **kwargs):
        if event == "end":
            store._last_say_ended = renpy.get_game_runtime()

    if _any_char_cb not in config.all_character_callbacks:
        config.all_character_callbacks.append(_any_char_cb)

    def ld_bg(bgname):
        bg_image = f"bgs/{bgname}.png"
        tag = "bg"

        if not renpy.loadable(bg_image):
            renpy.log(f"Couldn't load {tag} '{bgname}' from path '{bg_image}'")
            return False
        renpy.image((tag,bgname), bg_image)
    
    def ld_msc(mscname, alias):
        msc_file = f"audio/music/{mscname}.ogg"
        tag = "music"

        if not renpy.loadable(msc_file):
            renpy.log(f"Couldn't load {tag} '{mscname}' from path '{msc_file}'")
            return False
        setattr(store, f"music_{alias}", msc_file)
    
    def ld_amb(ambname, alias):
        amb_file = f"audio/ambience/{ambname}.ogg"
        tag = "ambience"

        if not renpy.loadable(amb_file):
            renpy.log(f"Couldn't load {tag} '{ambname}' from path '{amb_file}'")
            return False
        setattr(store, f"ambience_{alias}", amb_file)

    def ld_sfx(sfxname, alias):
        sfx_file = f"audio/sfx/{sfxname}.ogg"
        tag = "sfx"

        if not renpy.loadable(sfx_file):
            renpy.log(f"Couldn't load {tag} '{sfxname}' from path '{sfx_file}'")
            return False
        setattr(store, f"sfx_{alias}", sfx_file)

    # Background Files
    ld_bg("school_corridor")
    ld_bg("school_classroom")
    ld_bg("school_classroom_shiny")

    # Music Files
    ld_msc("Breathlessly", "peaceful")
    ld_msc("Caged_Heart", "future")
    ld_msc("Cold_Iron", "cold_as_iron")
    ld_msc("Comfort", "comfort_zone")
    ld_msc("Innocence", "happy_girl")
    ld_msc("Letting_my_Heart_Speak", "our_feelings")
    ld_msc("Moment_of_Decision", "distance")
    ld_msc("Wiosna", "relaxing")

    # Ambience
    ld_amb("wind_ambience", "corridor_wind")

    # SFX Files
    ld_sfx("tree-rustle", "tree_rustle")
    ld_sfx("tree-rustle-intense", "tree_rustle_intense")
    ld_sfx("tree-rustle-soft", "tree_rustle_soft")
    ld_sfx("wind-howl_1", "wind_howl_1")
    ld_sfx("wind-howl_2", "wind_howl_2")

    # Effects
    menueffect = None
    charchange = dissolve
    scenechange = dissolve
    contextchange = fade

    # Vars
    from_splash = False

    # Other functions
    def qc_menu(state: str) -> None:
        quick_menu = getattr(store, "quick_menu")

        if state == 'show':
            if not quick_menu:
                setattr(store, "quick_menu", True)
                return
        elif state == 'hide':
            if quick_menu:
                setattr(store, "quick_menu", False)
                return
        return

    def menu_init():
        renpy.music.play(music_relaxing, fadein=5.0, fadeout=0.5, if_changed=True)
    
    def set_channel_volume(channel, vol, delay=0.3, ignore=False):
        renpy.music.set_volume(vol, delay=delay, channel=channel,)
        if not ignore:
            channel_volumes[channel] = vol
    
    def get_channel_volume(channel):
        return channel_volumes.get(channel, 1.0)
    
    def amb_play(filename_or_list, fadein=1.0, if_changed=True, loop=True, synchro_start=False):
        """
        Plays or change current ambience music.
        - filename_or_list: string or string list/dictionary with filenames
        - fadein: how long to fade in (seconds)
        - if_changed: only change the current if different
        - loop: whether to loop the channel or not (will override the channel's default)
        """

        renpy.music.play(filename_or_list, 
        channel="ambience",
        fadein=fadein, 
        if_changed=if_changed, 
        loop=loop, 
        tight=True,
        synchro_start=synchro_start
        )

    def amb_stop(fadeout=1.0):
        renpy.music.stop(channel="ambience", fadeout=fadeout)
        
    def amb_volume(vol=1.0, delay=0.3):
        set_channel_volume("ambience", vol, delay)
    
    def amb_duck(to=0.35, delay=0.15):
        set_channel_volume("ambience", to, delay, ignore=True)
    
    def amb_unduck(delay=0.25):
        current = channel_volumes.get("ambience", 1.0)
        amb_volume(current, delay)
    
    def _menu_duck(start, duck_to=1.0, duck_delay=0.05):
        print(channel_volumes)
        if start:
            for ch in menu_duck_channels:
                try:
                    if ch in channel_volumes:
                        current = channel_volumes[ch]
                    else:
                        current = 1.0
                except Exception as e:
                    print(e)
                    current = 1.0

                if current < duck_to:
                    continue
                
                if current == duck_to:
                    duck_to = duck_to / 2
                
                # print(f"[MenuDuck] Channel '{ch}' volume {current} -> {duck_to}")
                renpy.music.set_volume(duck_to, duck_delay, channel=ch)
        else:
            for ch in menu_duck_channels:
                orig = channel_volumes.get(ch, 1.0)
                # print(f"[MenuDuck] Channel '{ch}' volume -> {orig}")
                renpy.music.set_volume(orig, duck_delay, channel=ch)

    # Classes
    # Fuck this class, fuck this shit, I hate it, I spent too much on this, idk why I overengineered something so simple, but it's done
    class SfxCycler(object):
        """
        items: list[dict] (each item):
            - "file": str | audio-var  (must-have)
            - "tags": str | list[str]  (optional; if empty -> "_any")
            - "vol":  float 0..1       (optional; default 1.0)

        interval: (min_s, max_s) interval for each sfx
        channel: which channel renpy gonna play
        rotation_tags: tags sequence to rotate between (case-insensitive)
            - If there is no available tags, continue
            - If empty, will look for any in the list
        """
        def __init__(self, items=None, interval=(20.0, 40.0), channel="ambfx", fadein=0.05, fadeout=0.05, rotation_tags=None, auto_rotation_mode="all"):

            self.channel = str(channel)
            self.fadein = max(0.0, float(fadein))
            self.fadeout = max(0.0, float(fadeout))

            self.interval = self._validate_interval(*interval)

            self._auto_mode = str(auto_rotation_mode or "none").lower()
            if rotation_tags:
                if isinstance(rotation_tags, (str, bytes)):
                    tag = str(rotation_tags).strip().lower()
                    self.rotation = [tag] if tag else []
                else:
                    self.rotation = [str(t).strip().lower() for t in rotation_tags if str(t).strip()]
                self._auto_mode = "none"
            else:
                self.rotation = []
            
            self._rot_idx = 0
            self.running = False

            self._set_items(items or [])
            self._refresh_rotation()
        
        # Debugg
        def _log(self, msg):
            renpy.log("[SfxCycler/%s] %s" % (self.channel, msg))

        # Setup
        def _validate_interval(self, a, b):
            a = float(a); b = float(b)
            if a < 0 or b < 0:
                raise ValueError("Interval values must be non-negative")
            if a > b:
                a, b = b, a
            return (a, b)

        def _mk_uid(self, f, tags, vol):
            tags_key = ",".join(sorted(t.lower() for t in (tags or [])))
            return f"{f}||{tags_key}||{round(float(vol), 3)}"

        def _normalize_items(self, items):
            norm = []
            for it in items or []:
                if not isinstance(it, dict): continue
                f = it.get("file", None)
                if f is None: continue
                
                raw_tags = it.get("tags", [])
                if isinstance(raw_tags, (str, bytes)):
                    raw_tags = [raw_tags]
                tags = {str(t).strip().lower() for t in raw_tags if str(t).strip()}
                if not tags:
                    tags = {"_any"}
                
                vol = max(0.0, min(1.0, float(it.get("vol", 1.0))))

                uid = self._mk_uid(str(f), tags, vol)
                norm.append({"file": f, "tags": tags, "vol": vol, "uid": uid})

            return norm
        
        def _rebuild_indexes(self):
            self.by_tag = {}
            for it in self.items:
                for t in it["tags"]:
                    self.by_tag.setdefault(t, []).append(it)
            self._rebuild_queues(reset_used=False)
        
        def _rebuild_queues(self, reset_used):
            if reset_used:
                self.used = set()

            self.queues = {}
            for tag, lst in self.by_tag.items():
                pool = [it for it in lst if it["uid"] not in self.used]
                renpy.random.shuffle(pool)
                self.queues[tag] = deque(pool)
            
            all_tags = list(self.by_tag.keys())
            renpy.random.shuffle(all_tags)
            if "_any" in all_tags:
                all_tags.remove("_any")
                all_tags.append("_any")
            self._all_tags_order = all_tags

        def _set_items(self, items):
            self.items = self._normalize_items(items)
            self.used = set()
            self._rebuild_indexes()

        # Tag rotation
        def _derive_rotation_from_items(self):
            """
            self._auto_mode has three options:
                - "none": no auto-rotation / []
                - "all": rotate between all available tags in order of appearance
                - "top2": rotate between two most common tags in order of appearance
            """
            if self._auto_mode == "none":
                return []

            order, counts, seen = [], {}, set()

            for it in self.items:
                for t in it["tags"]:
                    if t == "_any": continue
                    counts[t] = counts.get(t, 0) + 1
                    if t not in seen:
                        seen.add(t); order.append(t)
            if not order:
                return []

            if self._auto_mode == "all":
                return order

            if self._auto_mode == "top2":
                ranked = sorted(counts.items(), key=lambda kv: (-kv[1], order.index(kv[0])))
                return [t for (t, _) in ranked[:2]]
            
            return order

        def _refresh_rotation(self):
            if self._auto_mode == "none":
                return

            self.rotation = self._derive_rotation_from_items()
            self._rot_idx = 0

        def _queue_pick_from_tag(self, tag):
            q = self.queues.get(tag)
            if not q:
                return None

            while q:
                it = q.popleft()
                if it["uid"] not in self.used:
                    return it

            remaining = any(it["uid"] not in self.used for it in self.items)
            if remaining:
                self._rebuild_queues(reset_used=False)
                q = self.queues.get(tag)
                if q:
                    while q:
                        it = q.popleft()
                        if it["uid"] not in self.used:
                            return it
            return None

        def _rotation_peek_tag(self):
            if not self.rotation:
                return None
            return self.rotation[self._rot_idx % len(self.rotation)]

        def _rotation_advance(self):
            if self.rotation:
                self._rot_idx = (self._rot_idx + 1) % len(self.rotation)
        
        def _pick_next_item(self):
            tried = set()

            if self.rotation:
                for _ in range(len(self.rotation)):
                    tag = self._rotation_peek_tag()
                    if tag in tried:
                        self._rotation_advance(); continue
                    tried.add(tag)

                    it = self._queue_pick_from_tag(tag)
                    if it:
                        self._rotation_advance()
                        return it, tag
                    else:
                        self._rotation_advance()
                
            for t in self._all_tags_order:
                it = self._queue_pick_from_tag(t)
                if it:
                    return it, t
            
            if self.items:
                self._rebuild_queues(reset_used=True)

                for t in self._all_tags_order:
                    it = self._queue_pick_from_tag(t)
                    if it:
                        return it, t

            return None

        def _build_spec(self, it, delay):
            return ["<silence %.3f>" % float(delay), it["file"]]          

        def _on_queue_empty(self):
            if not self.running: 
                return

            pick = self._pick_next_item()
            if not pick:
                self.running = False
                return

            it, tag = pick
            self.used.add(it["uid"])

            delay = renpy.random.uniform(self.interval[0], self.interval[1])
            
            renpy.music.queue(
                self._build_spec(it, delay),
                channel=self.channel,
                loop=False,
                tight=True,
                fadein=self.fadein,
                relative_volume=float(it["vol"])
            )

        # Control
        def start(self, start_after_random=True):
            if self.running:
                return
            
            if not self.items:
                return

            self.running = True
            self._rebuild_queues(reset_used=False)
            self._refresh_rotation()

            self._ctx = renpy.context()

            renpy.music.set_queue_empty_callback(self._on_queue_empty, channel=self.channel)
   
        def stop(self, stop_all=False):
            self.running = False
            renpy.music.set_queue_empty_callback(None, channel=self.channel)

            if stop_all:
                renpy.music.stop(channel=self.channel, fadeout=self.fadeout)

        def set_interval(self, min_s, max_s):
            self.interval = self._validate_interval(min_s, max_s)
            
        def set_items(self, items, reset_cycle=True):
            self._set_items(items)
            if reset_cycle:
                self._rot_idx = 0
            
            self._refresh_rotation()

        def set_rotation_tags(self, *tags):
            if not tags:
                self.rotation = []; self._auto_mode = "none"
            else:
                self.rotation = [str(t).strip().lower() for t in tags if str(t).strip()]
                self._auto_mode = "none"

            self._rot_idx = 0
        
        def set_auto_rotation_mode(self, mode):
            """
            Change auto-rotation mode.
            mode: "none" | "all" | "top2"
            """

            self._auto_mode = str(mode or "none").lower()
            self._refresh_rotation()
            self._rot_idx = 0

        
        def is_running(self):
            return self.running