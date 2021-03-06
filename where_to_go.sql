PGDMP          7                y            where_to_go    12.6    12.6 &    ,           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            -           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            .           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            /           1262    16393    where_to_go    DATABASE     �   CREATE DATABASE where_to_go WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Russian_Russia.1251' LC_CTYPE = 'Russian_Russia.1251';
    DROP DATABASE where_to_go;
                postgres    false            �            1259    16583    favorite_place    TABLE     �   CREATE TABLE public.favorite_place (
    person_id integer NOT NULL,
    place_id integer NOT NULL,
    rate numeric(1,0) NOT NULL
);
 "   DROP TABLE public.favorite_place;
       public         heap    postgres    false            �            1259    16579    favorite_place_person_id_seq    SEQUENCE     �   CREATE SEQUENCE public.favorite_place_person_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.favorite_place_person_id_seq;
       public          postgres    false    210            0           0    0    favorite_place_person_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.favorite_place_person_id_seq OWNED BY public.favorite_place.person_id;
          public          postgres    false    208            �            1259    16581    favorite_place_place_id_seq    SEQUENCE     �   CREATE SEQUENCE public.favorite_place_place_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.favorite_place_place_id_seq;
       public          postgres    false    210            1           0    0    favorite_place_place_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.favorite_place_place_id_seq OWNED BY public.favorite_place.place_id;
          public          postgres    false    209            �            1259    16520    person    TABLE     �   CREATE TABLE public.person (
    person_id integer NOT NULL,
    name text NOT NULL,
    surname text NOT NULL,
    patronymic text NOT NULL,
    bday date NOT NULL
);
    DROP TABLE public.person;
       public         heap    postgres    false            �            1259    16518    person_person_id_seq    SEQUENCE     �   CREATE SEQUENCE public.person_person_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.person_person_id_seq;
       public          postgres    false    203            2           0    0    person_person_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.person_person_id_seq OWNED BY public.person.person_id;
          public          postgres    false    202            �            1259    16532    place    TABLE     
  CREATE TABLE public.place (
    place_id integer NOT NULL,
    name character(25) NOT NULL,
    adress character varying(100) NOT NULL,
    description character varying(255) NOT NULL,
    rate numeric(1,0) NOT NULL,
    photo_src character varying(100) NOT NULL
);
    DROP TABLE public.place;
       public         heap    postgres    false            �            1259    16565    place_category    TABLE     b   CREATE TABLE public.place_category (
    place_id integer NOT NULL,
    category text NOT NULL
);
 "   DROP TABLE public.place_category;
       public         heap    postgres    false            �            1259    16563    place_category_place_id_seq    SEQUENCE     �   CREATE SEQUENCE public.place_category_place_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.place_category_place_id_seq;
       public          postgres    false    207            3           0    0    place_category_place_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.place_category_place_id_seq OWNED BY public.place_category.place_id;
          public          postgres    false    206            �            1259    16530    place_place_id_seq    SEQUENCE     �   CREATE SEQUENCE public.place_place_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.place_place_id_seq;
       public          postgres    false    205            4           0    0    place_place_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.place_place_id_seq OWNED BY public.place.place_id;
          public          postgres    false    204            �
           2604    16586    favorite_place person_id    DEFAULT     �   ALTER TABLE ONLY public.favorite_place ALTER COLUMN person_id SET DEFAULT nextval('public.favorite_place_person_id_seq'::regclass);
 G   ALTER TABLE public.favorite_place ALTER COLUMN person_id DROP DEFAULT;
       public          postgres    false    208    210    210            �
           2604    16587    favorite_place place_id    DEFAULT     �   ALTER TABLE ONLY public.favorite_place ALTER COLUMN place_id SET DEFAULT nextval('public.favorite_place_place_id_seq'::regclass);
 F   ALTER TABLE public.favorite_place ALTER COLUMN place_id DROP DEFAULT;
       public          postgres    false    209    210    210            �
           2604    16523    person person_id    DEFAULT     t   ALTER TABLE ONLY public.person ALTER COLUMN person_id SET DEFAULT nextval('public.person_person_id_seq'::regclass);
 ?   ALTER TABLE public.person ALTER COLUMN person_id DROP DEFAULT;
       public          postgres    false    203    202    203            �
           2604    16535    place place_id    DEFAULT     p   ALTER TABLE ONLY public.place ALTER COLUMN place_id SET DEFAULT nextval('public.place_place_id_seq'::regclass);
 =   ALTER TABLE public.place ALTER COLUMN place_id DROP DEFAULT;
       public          postgres    false    205    204    205            �
           2604    16568    place_category place_id    DEFAULT     �   ALTER TABLE ONLY public.place_category ALTER COLUMN place_id SET DEFAULT nextval('public.place_category_place_id_seq'::regclass);
 F   ALTER TABLE public.place_category ALTER COLUMN place_id DROP DEFAULT;
       public          postgres    false    206    207    207            )          0    16583    favorite_place 
   TABLE DATA           C   COPY public.favorite_place (person_id, place_id, rate) FROM stdin;
    public          postgres    false    210   �+       "          0    16520    person 
   TABLE DATA           L   COPY public.person (person_id, name, surname, patronymic, bday) FROM stdin;
    public          postgres    false    203   �+       $          0    16532    place 
   TABLE DATA           U   COPY public.place (place_id, name, adress, description, rate, photo_src) FROM stdin;
    public          postgres    false    205   ,       &          0    16565    place_category 
   TABLE DATA           <   COPY public.place_category (place_id, category) FROM stdin;
    public          postgres    false    207   .       5           0    0    favorite_place_person_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.favorite_place_person_id_seq', 1, false);
          public          postgres    false    208            6           0    0    favorite_place_place_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.favorite_place_place_id_seq', 1, false);
          public          postgres    false    209            7           0    0    person_person_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.person_person_id_seq', 1, true);
          public          postgres    false    202            8           0    0    place_category_place_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.place_category_place_id_seq', 1, false);
          public          postgres    false    206            9           0    0    place_place_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.place_place_id_seq', 8, true);
          public          postgres    false    204            �
           2606    16599 "   favorite_place favorite_place_pkey 
   CONSTRAINT     q   ALTER TABLE ONLY public.favorite_place
    ADD CONSTRAINT favorite_place_pkey PRIMARY KEY (person_id, place_id);
 L   ALTER TABLE ONLY public.favorite_place DROP CONSTRAINT favorite_place_pkey;
       public            postgres    false    210    210            �
           2606    16528    person person_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.person
    ADD CONSTRAINT person_pkey PRIMARY KEY (person_id);
 <   ALTER TABLE ONLY public.person DROP CONSTRAINT person_pkey;
       public            postgres    false    203            �
           2606    16540    place place_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.place
    ADD CONSTRAINT place_pkey PRIMARY KEY (place_id);
 :   ALTER TABLE ONLY public.place DROP CONSTRAINT place_pkey;
       public            postgres    false    205            �
           2606    16588 ,   favorite_place favorite_place_person_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.favorite_place
    ADD CONSTRAINT favorite_place_person_id_fkey FOREIGN KEY (person_id) REFERENCES public.person(person_id);
 V   ALTER TABLE ONLY public.favorite_place DROP CONSTRAINT favorite_place_person_id_fkey;
       public          postgres    false    203    2715    210            �
           2606    16593 +   favorite_place favorite_place_place_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.favorite_place
    ADD CONSTRAINT favorite_place_place_id_fkey FOREIGN KEY (place_id) REFERENCES public.place(place_id);
 U   ALTER TABLE ONLY public.favorite_place DROP CONSTRAINT favorite_place_place_id_fkey;
       public          postgres    false    210    205    2717            �
           2606    16572 +   place_category place_category_place_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.place_category
    ADD CONSTRAINT place_category_place_id_fkey FOREIGN KEY (place_id) REFERENCES public.place(place_id);
 U   ALTER TABLE ONLY public.place_category DROP CONSTRAINT place_category_place_id_fkey;
       public          postgres    false    205    2717    207            )      x�3�4�4�2�4������� k      "   ?   x�3�0���=�9/,��p��b煭6�D7_�w�Ĺ��b;����������!W� ґ�      $   �  x����N"A��{��oɬ=���� 躉ƿK���;�m�W�~�=��,�^-]�_�:U��j�5�J���y�y9}�&N�Lߵ@�Q�j�K���x�KNz�i��;�CRe -�d��G�5�>��H*�U�S�ϴq�T|�L����Y?�Hn����?�^�0�z�O\˺�N�D6�t���>Bq�����-�|	4�BSib���]#��������|H����X�W�'*dI��[�Q��h�R7r��'C�HY�*�H/��{�bw���0x�GC�v���9�w�a�x�t"0��,� W;�@��.�7���7U_p�C���7@ц���N��p��-��x��m)pk�l�7�)��KwF��[.������>�V�2���[ɇQmu\�M�����b�q��c�`P�ឯq�ی޶��r.�m6�+܁���,��B{00����h�잱{\X�:ڈܧʹ�xN;>�$m�LP�'?�$I��Nc       &   Q   x�3�0�¾�-�^�ya��~.#���{��M@��.6�\�pa��Mv_�z�(�����y@u[.v_l����� #@0_     