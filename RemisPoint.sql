PGDMP  8                	    {         
   RemisPoint    16.0    16.0 b    &           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            '           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            (           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            )           1262    16401 
   RemisPoint    DATABASE        CREATE DATABASE "RemisPoint" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Spain.1252';
    DROP DATABASE "RemisPoint";
                postgres    false            �            1259    16444    Autos    TABLE       CREATE TABLE public."Autos" (
    patente character varying NOT NULL,
    tipo character varying,
    foto character varying,
    anio_modelo integer,
    propietario character varying,
    vtv character varying,
    venc_patente character varying,
    id_remiseria integer
);
    DROP TABLE public."Autos";
       public         heap    postgres    false            �            1259    16462    Chofer    TABLE     �   CREATE TABLE public."Chofer" (
    id_chofer integer NOT NULL,
    nombre character varying,
    apellido character varying,
    nro_tel character varying,
    licencia "char"
);
    DROP TABLE public."Chofer";
       public         heap    postgres    false            �            1259    16456 
   ChoferAuto    TABLE     z   CREATE TABLE public."ChoferAuto" (
    patente character varying,
    id_chofer integer,
    "Turno" character varying
);
     DROP TABLE public."ChoferAuto";
       public         heap    postgres    false            �            1259    16461    Chofer_id_chofer_seq    SEQUENCE     �   CREATE SEQUENCE public."Chofer_id_chofer_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public."Chofer_id_chofer_seq";
       public          postgres    false    232            *           0    0    Chofer_id_chofer_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public."Chofer_id_chofer_seq" OWNED BY public."Chofer".id_chofer;
          public          postgres    false    231            �            1259    16431    Clientes    TABLE       CREATE TABLE public."Clientes" (
    id_cliente integer NOT NULL,
    nombre character varying,
    id_localidad integer,
    telefono character varying,
    direccion character varying,
    correo character varying,
    password character varying,
    tipo_cuenta integer
);
    DROP TABLE public."Clientes";
       public         heap    postgres    false            �            1259    16430    Clientes_id_cliente_seq    SEQUENCE     �   CREATE SEQUENCE public."Clientes_id_cliente_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public."Clientes_id_cliente_seq";
       public          postgres    false    224            +           0    0    Clientes_id_cliente_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public."Clientes_id_cliente_seq" OWNED BY public."Clientes".id_cliente;
          public          postgres    false    223            �            1259    16438 	   Localidad    TABLE     e   CREATE TABLE public."Localidad" (
    id_localidad integer NOT NULL,
    nombre character varying
);
    DROP TABLE public."Localidad";
       public         heap    postgres    false            �            1259    16437    Localidad_id_localidad_seq    SEQUENCE     �   CREATE SEQUENCE public."Localidad_id_localidad_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public."Localidad_id_localidad_seq";
       public          postgres    false    226            ,           0    0    Localidad_id_localidad_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public."Localidad_id_localidad_seq" OWNED BY public."Localidad".id_localidad;
          public          postgres    false    225            �            1259    16410    Precio    TABLE     �   CREATE TABLE public."Precio" (
    id_precio integer NOT NULL,
    descripcion character varying,
    kmdesde double precision,
    kmhasta double precision,
    precio integer,
    interes integer
);
    DROP TABLE public."Precio";
       public         heap    postgres    false            �            1259    16409    Precio_id_precio_seq    SEQUENCE     �   CREATE SEQUENCE public."Precio_id_precio_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public."Precio_id_precio_seq";
       public          postgres    false    218            -           0    0    Precio_id_precio_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public."Precio_id_precio_seq" OWNED BY public."Precio".id_precio;
          public          postgres    false    217            �            1259    16555    Recordatorios    TABLE     �   CREATE TABLE public."Recordatorios" (
    cod_recordatorio integer NOT NULL,
    id_cliente integer,
    dia date,
    hora time without time zone,
    direccion character varying,
    patente character varying
);
 #   DROP TABLE public."Recordatorios";
       public         heap    postgres    false            �            1259    16554 "   Recordatorios_cod_recordatorio_seq    SEQUENCE     �   CREATE SEQUENCE public."Recordatorios_cod_recordatorio_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ;   DROP SEQUENCE public."Recordatorios_cod_recordatorio_seq";
       public          postgres    false    234            .           0    0 "   Recordatorios_cod_recordatorio_seq    SEQUENCE OWNED BY     m   ALTER SEQUENCE public."Recordatorios_cod_recordatorio_seq" OWNED BY public."Recordatorios".cod_recordatorio;
          public          postgres    false    233            �            1259    16450    Registro    TABLE     �   CREATE TABLE public."Registro" (
    id_registro integer NOT NULL,
    patente character varying,
    fecha date,
    ingreso time without time zone,
    egreso time with time zone,
    id_chofer integer
);
    DROP TABLE public."Registro";
       public         heap    postgres    false            �            1259    16449    Registro_id_registro_seq    SEQUENCE     �   CREATE SEQUENCE public."Registro_id_registro_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public."Registro_id_registro_seq";
       public          postgres    false    229            /           0    0    Registro_id_registro_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public."Registro_id_registro_seq" OWNED BY public."Registro".id_registro;
          public          postgres    false    228            �            1259    16424 	   Remiseria    TABLE     �   CREATE TABLE public."Remiseria" (
    id_remiseria integer NOT NULL,
    nombre character varying,
    telefono character varying,
    foto "char"
);
    DROP TABLE public."Remiseria";
       public         heap    postgres    false            �            1259    16423    Remiseria_id_remiseria_seq    SEQUENCE     �   CREATE SEQUENCE public."Remiseria_id_remiseria_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public."Remiseria_id_remiseria_seq";
       public          postgres    false    222            0           0    0    Remiseria_id_remiseria_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public."Remiseria_id_remiseria_seq" OWNED BY public."Remiseria".id_remiseria;
          public          postgres    false    221            �            1259    16417    TipoPago    TABLE     j   CREATE TABLE public."TipoPago" (
    cod_tipo_pago integer NOT NULL,
    descripcion character varying
);
    DROP TABLE public."TipoPago";
       public         heap    postgres    false            �            1259    16416    TipoPago_cod_tipo_pago_seq    SEQUENCE     �   CREATE SEQUENCE public."TipoPago_cod_tipo_pago_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public."TipoPago_cod_tipo_pago_seq";
       public          postgres    false    220            1           0    0    TipoPago_cod_tipo_pago_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public."TipoPago_cod_tipo_pago_seq" OWNED BY public."TipoPago".cod_tipo_pago;
          public          postgres    false    219            �            1259    16403    Viajes    TABLE     |  CREATE TABLE public."Viajes" (
    id_viaje integer NOT NULL,
    id_cliente integer,
    dir_salida character varying,
    dir_destino character varying,
    hora time without time zone,
    fecha date,
    id_precio integer,
    cod_tipo_pago integer,
    id_remiseria integer,
    inicio time without time zone,
    fin time without time zone,
    patente character varying
);
    DROP TABLE public."Viajes";
       public         heap    postgres    false            �            1259    16402    Viajes_id_viaje_seq    SEQUENCE     �   CREATE SEQUENCE public."Viajes_id_viaje_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public."Viajes_id_viaje_seq";
       public          postgres    false    216            2           0    0    Viajes_id_viaje_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public."Viajes_id_viaje_seq" OWNED BY public."Viajes".id_viaje;
          public          postgres    false    215            Q           2604    16465    Chofer id_chofer    DEFAULT     x   ALTER TABLE ONLY public."Chofer" ALTER COLUMN id_chofer SET DEFAULT nextval('public."Chofer_id_chofer_seq"'::regclass);
 A   ALTER TABLE public."Chofer" ALTER COLUMN id_chofer DROP DEFAULT;
       public          postgres    false    232    231    232            N           2604    16434    Clientes id_cliente    DEFAULT     ~   ALTER TABLE ONLY public."Clientes" ALTER COLUMN id_cliente SET DEFAULT nextval('public."Clientes_id_cliente_seq"'::regclass);
 D   ALTER TABLE public."Clientes" ALTER COLUMN id_cliente DROP DEFAULT;
       public          postgres    false    224    223    224            O           2604    16441    Localidad id_localidad    DEFAULT     �   ALTER TABLE ONLY public."Localidad" ALTER COLUMN id_localidad SET DEFAULT nextval('public."Localidad_id_localidad_seq"'::regclass);
 G   ALTER TABLE public."Localidad" ALTER COLUMN id_localidad DROP DEFAULT;
       public          postgres    false    225    226    226            K           2604    16413    Precio id_precio    DEFAULT     x   ALTER TABLE ONLY public."Precio" ALTER COLUMN id_precio SET DEFAULT nextval('public."Precio_id_precio_seq"'::regclass);
 A   ALTER TABLE public."Precio" ALTER COLUMN id_precio DROP DEFAULT;
       public          postgres    false    218    217    218            R           2604    16558    Recordatorios cod_recordatorio    DEFAULT     �   ALTER TABLE ONLY public."Recordatorios" ALTER COLUMN cod_recordatorio SET DEFAULT nextval('public."Recordatorios_cod_recordatorio_seq"'::regclass);
 O   ALTER TABLE public."Recordatorios" ALTER COLUMN cod_recordatorio DROP DEFAULT;
       public          postgres    false    234    233    234            P           2604    16453    Registro id_registro    DEFAULT     �   ALTER TABLE ONLY public."Registro" ALTER COLUMN id_registro SET DEFAULT nextval('public."Registro_id_registro_seq"'::regclass);
 E   ALTER TABLE public."Registro" ALTER COLUMN id_registro DROP DEFAULT;
       public          postgres    false    229    228    229            M           2604    16427    Remiseria id_remiseria    DEFAULT     �   ALTER TABLE ONLY public."Remiseria" ALTER COLUMN id_remiseria SET DEFAULT nextval('public."Remiseria_id_remiseria_seq"'::regclass);
 G   ALTER TABLE public."Remiseria" ALTER COLUMN id_remiseria DROP DEFAULT;
       public          postgres    false    222    221    222            L           2604    16420    TipoPago cod_tipo_pago    DEFAULT     �   ALTER TABLE ONLY public."TipoPago" ALTER COLUMN cod_tipo_pago SET DEFAULT nextval('public."TipoPago_cod_tipo_pago_seq"'::regclass);
 G   ALTER TABLE public."TipoPago" ALTER COLUMN cod_tipo_pago DROP DEFAULT;
       public          postgres    false    219    220    220            J           2604    16406    Viajes id_viaje    DEFAULT     v   ALTER TABLE ONLY public."Viajes" ALTER COLUMN id_viaje SET DEFAULT nextval('public."Viajes_id_viaje_seq"'::regclass);
 @   ALTER TABLE public."Viajes" ALTER COLUMN id_viaje DROP DEFAULT;
       public          postgres    false    215    216    216                      0    16444    Autos 
   TABLE DATA           q   COPY public."Autos" (patente, tipo, foto, anio_modelo, propietario, vtv, venc_patente, id_remiseria) FROM stdin;
    public          postgres    false    227   �t       !          0    16462    Chofer 
   TABLE DATA           R   COPY public."Chofer" (id_chofer, nombre, apellido, nro_tel, licencia) FROM stdin;
    public          postgres    false    232   �t                 0    16456 
   ChoferAuto 
   TABLE DATA           C   COPY public."ChoferAuto" (patente, id_chofer, "Turno") FROM stdin;
    public          postgres    false    230   �t                 0    16431    Clientes 
   TABLE DATA           z   COPY public."Clientes" (id_cliente, nombre, id_localidad, telefono, direccion, correo, password, tipo_cuenta) FROM stdin;
    public          postgres    false    224   u                 0    16438 	   Localidad 
   TABLE DATA           ;   COPY public."Localidad" (id_localidad, nombre) FROM stdin;
    public          postgres    false    226   �u                 0    16410    Precio 
   TABLE DATA           ]   COPY public."Precio" (id_precio, descripcion, kmdesde, kmhasta, precio, interes) FROM stdin;
    public          postgres    false    218   �u       #          0    16555    Recordatorios 
   TABLE DATA           f   COPY public."Recordatorios" (cod_recordatorio, id_cliente, dia, hora, direccion, patente) FROM stdin;
    public          postgres    false    234   �u                 0    16450    Registro 
   TABLE DATA           ]   COPY public."Registro" (id_registro, patente, fecha, ingreso, egreso, id_chofer) FROM stdin;
    public          postgres    false    229   v                 0    16424 	   Remiseria 
   TABLE DATA           K   COPY public."Remiseria" (id_remiseria, nombre, telefono, foto) FROM stdin;
    public          postgres    false    222   /v                 0    16417    TipoPago 
   TABLE DATA           @   COPY public."TipoPago" (cod_tipo_pago, descripcion) FROM stdin;
    public          postgres    false    220   Lv                 0    16403    Viajes 
   TABLE DATA           �   COPY public."Viajes" (id_viaje, id_cliente, dir_salida, dir_destino, hora, fecha, id_precio, cod_tipo_pago, id_remiseria, inicio, fin, patente) FROM stdin;
    public          postgres    false    216   iv       3           0    0    Chofer_id_chofer_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public."Chofer_id_chofer_seq"', 1, false);
          public          postgres    false    231            4           0    0    Clientes_id_cliente_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public."Clientes_id_cliente_seq"', 2, true);
          public          postgres    false    223            5           0    0    Localidad_id_localidad_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public."Localidad_id_localidad_seq"', 7, true);
          public          postgres    false    225            6           0    0    Precio_id_precio_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public."Precio_id_precio_seq"', 1, false);
          public          postgres    false    217            7           0    0 "   Recordatorios_cod_recordatorio_seq    SEQUENCE SET     S   SELECT pg_catalog.setval('public."Recordatorios_cod_recordatorio_seq"', 1, false);
          public          postgres    false    233            8           0    0    Registro_id_registro_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public."Registro_id_registro_seq"', 1, false);
          public          postgres    false    228            9           0    0    Remiseria_id_remiseria_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public."Remiseria_id_remiseria_seq"', 1, false);
          public          postgres    false    221            :           0    0    TipoPago_cod_tipo_pago_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public."TipoPago_cod_tipo_pago_seq"', 1, false);
          public          postgres    false    219            ;           0    0    Viajes_id_viaje_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public."Viajes_id_viaje_seq"', 1, false);
          public          postgres    false    215            ]           2606    16491    TipoPago pK_TipoPago 
   CONSTRAINT     a   ALTER TABLE ONLY public."TipoPago"
    ADD CONSTRAINT "pK_TipoPago" PRIMARY KEY (cod_tipo_pago);
 B   ALTER TABLE ONLY public."TipoPago" DROP CONSTRAINT "pK_TipoPago";
       public            postgres    false    220            s           2606    16562 !   Recordatorios pK_cod_Recordatorio 
   CONSTRAINT     q   ALTER TABLE ONLY public."Recordatorios"
    ADD CONSTRAINT "pK_cod_Recordatorio" PRIMARY KEY (cod_recordatorio);
 O   ALTER TABLE ONLY public."Recordatorios" DROP CONSTRAINT "pK_cod_Recordatorio";
       public            postgres    false    234            b           2606    16469    Clientes pK_idCliente 
   CONSTRAINT     _   ALTER TABLE ONLY public."Clientes"
    ADD CONSTRAINT "pK_idCliente" PRIMARY KEY (id_cliente);
 C   ALTER TABLE ONLY public."Clientes" DROP CONSTRAINT "pK_idCliente";
       public            postgres    false    224            d           2606    16479    Localidad pK_idLocalidad 
   CONSTRAINT     d   ALTER TABLE ONLY public."Localidad"
    ADD CONSTRAINT "pK_idLocalidad" PRIMARY KEY (id_localidad);
 F   ALTER TABLE ONLY public."Localidad" DROP CONSTRAINT "pK_idLocalidad";
       public            postgres    false    226            k           2606    16489    Registro pK_idRegistro 
   CONSTRAINT     a   ALTER TABLE ONLY public."Registro"
    ADD CONSTRAINT "pK_idRegistro" PRIMARY KEY (id_registro);
 D   ALTER TABLE ONLY public."Registro" DROP CONSTRAINT "pK_idRegistro";
       public            postgres    false    229            Y           2606    16493    Viajes pK_idViaje 
   CONSTRAINT     Y   ALTER TABLE ONLY public."Viajes"
    ADD CONSTRAINT "pK_idViaje" PRIMARY KEY (id_viaje);
 ?   ALTER TABLE ONLY public."Viajes" DROP CONSTRAINT "pK_idViaje";
       public            postgres    false    216            o           2606    16481    Chofer pk_idChofer 
   CONSTRAINT     [   ALTER TABLE ONLY public."Chofer"
    ADD CONSTRAINT "pk_idChofer" PRIMARY KEY (id_chofer);
 @   ALTER TABLE ONLY public."Chofer" DROP CONSTRAINT "pk_idChofer";
       public            postgres    false    232            [           2606    16487    Precio pk_idPrecio 
   CONSTRAINT     [   ALTER TABLE ONLY public."Precio"
    ADD CONSTRAINT "pk_idPrecio" PRIMARY KEY (id_precio);
 @   ALTER TABLE ONLY public."Precio" DROP CONSTRAINT "pk_idPrecio";
       public            postgres    false    218            _           2606    16477    Remiseria pk_idRemiseria 
   CONSTRAINT     d   ALTER TABLE ONLY public."Remiseria"
    ADD CONSTRAINT "pk_idRemiseria" PRIMARY KEY (id_remiseria);
 F   ALTER TABLE ONLY public."Remiseria" DROP CONSTRAINT "pk_idRemiseria";
       public            postgres    false    222            g           2606    16483    Autos pk_patente 
   CONSTRAINT     U   ALTER TABLE ONLY public."Autos"
    ADD CONSTRAINT pk_patente PRIMARY KEY (patente);
 <   ALTER TABLE ONLY public."Autos" DROP CONSTRAINT pk_patente;
       public            postgres    false    227            l           1259    16517    fki_F    INDEX     E   CREATE INDEX "fki_F" ON public."ChoferAuto" USING btree (id_chofer);
    DROP INDEX public."fki_F";
       public            postgres    false    230            e           1259    16529    fki_d    INDEX     A   CREATE INDEX fki_d ON public."Autos" USING btree (id_remiseria);
    DROP INDEX public.fki_d;
       public            postgres    false    227            h           1259    16553    fki_fK_Chofer_Registro    INDEX     T   CREATE INDEX "fki_fK_Chofer_Registro" ON public."Registro" USING btree (id_chofer);
 ,   DROP INDEX public."fki_fK_Chofer_Registro";
       public            postgres    false    229            p           1259    16575    fki_fK_Cliente_Record    INDEX     Y   CREATE INDEX "fki_fK_Cliente_Record" ON public."Recordatorios" USING btree (id_cliente);
 +   DROP INDEX public."fki_fK_Cliente_Record";
       public            postgres    false    234            `           1259    16511    fki_fK_Id_localidad    INDEX     T   CREATE INDEX "fki_fK_Id_localidad" ON public."Clientes" USING btree (id_localidad);
 )   DROP INDEX public."fki_fK_Id_localidad";
       public            postgres    false    224            S           1259    16475    fki_fK_idCliente    INDEX     M   CREATE INDEX "fki_fK_idCliente" ON public."Viajes" USING btree (id_cliente);
 &   DROP INDEX public."fki_fK_idCliente";
       public            postgres    false    216            T           1259    16541    fki_fK_idRemiseria_Viajes    INDEX     X   CREATE INDEX "fki_fK_idRemiseria_Viajes" ON public."Viajes" USING btree (id_remiseria);
 /   DROP INDEX public."fki_fK_idRemiseria_Viajes";
       public            postgres    false    216            U           1259    16499    fki_fK_patente    INDEX     H   CREATE INDEX "fki_fK_patente" ON public."Viajes" USING btree (patente);
 $   DROP INDEX public."fki_fK_patente";
       public            postgres    false    216            m           1259    16523    fki_fK_patente_CA    INDEX     O   CREATE INDEX "fki_fK_patente_CA" ON public."ChoferAuto" USING btree (patente);
 '   DROP INDEX public."fki_fK_patente_CA";
       public            postgres    false    230            q           1259    16568    fki_fK_patente_Record    INDEX     V   CREATE INDEX "fki_fK_patente_Record" ON public."Recordatorios" USING btree (patente);
 +   DROP INDEX public."fki_fK_patente_Record";
       public            postgres    false    234            V           1259    16547    fki_fK_tipoPago_Viajes    INDEX     V   CREATE INDEX "fki_fK_tipoPago_Viajes" ON public."Viajes" USING btree (cod_tipo_pago);
 ,   DROP INDEX public."fki_fK_tipoPago_Viajes";
       public            postgres    false    216            W           1259    16505    fki_fk_idPrecio    INDEX     K   CREATE INDEX "fki_fk_idPrecio" ON public."Viajes" USING btree (id_precio);
 %   DROP INDEX public."fki_fk_idPrecio";
       public            postgres    false    216            i           1259    16535    fki_pK_Patente_Registro    INDEX     S   CREATE INDEX "fki_pK_Patente_Registro" ON public."Registro" USING btree (patente);
 -   DROP INDEX public."fki_pK_Patente_Registro";
       public            postgres    false    229            {           2606    16548    Registro fK_Chofer_Registro    FK CONSTRAINT     �   ALTER TABLE ONLY public."Registro"
    ADD CONSTRAINT "fK_Chofer_Registro" FOREIGN KEY (id_chofer) REFERENCES public."Chofer"(id_chofer);
 I   ALTER TABLE ONLY public."Registro" DROP CONSTRAINT "fK_Chofer_Registro";
       public          postgres    false    229    4719    232                       2606    16570    Recordatorios fK_Cliente_Record    FK CONSTRAINT     �   ALTER TABLE ONLY public."Recordatorios"
    ADD CONSTRAINT "fK_Cliente_Record" FOREIGN KEY (id_cliente) REFERENCES public."Clientes"(id_cliente);
 M   ALTER TABLE ONLY public."Recordatorios" DROP CONSTRAINT "fK_Cliente_Record";
       public          postgres    false    4706    234    224            y           2606    16506    Clientes fK_Id_localidad    FK CONSTRAINT     �   ALTER TABLE ONLY public."Clientes"
    ADD CONSTRAINT "fK_Id_localidad" FOREIGN KEY (id_localidad) REFERENCES public."Localidad"(id_localidad);
 F   ALTER TABLE ONLY public."Clientes" DROP CONSTRAINT "fK_Id_localidad";
       public          postgres    false    224    4708    226            t           2606    16470    Viajes fK_idCliente    FK CONSTRAINT     �   ALTER TABLE ONLY public."Viajes"
    ADD CONSTRAINT "fK_idCliente" FOREIGN KEY (id_cliente) REFERENCES public."Clientes"(id_cliente);
 A   ALTER TABLE ONLY public."Viajes" DROP CONSTRAINT "fK_idCliente";
       public          postgres    false    216    4706    224            z           2606    16524    Autos fK_idRemiseria_Autos    FK CONSTRAINT     �   ALTER TABLE ONLY public."Autos"
    ADD CONSTRAINT "fK_idRemiseria_Autos" FOREIGN KEY (id_remiseria) REFERENCES public."Remiseria"(id_remiseria);
 H   ALTER TABLE ONLY public."Autos" DROP CONSTRAINT "fK_idRemiseria_Autos";
       public          postgres    false    222    4703    227            u           2606    16536    Viajes fK_idRemiseria_Viajes    FK CONSTRAINT     �   ALTER TABLE ONLY public."Viajes"
    ADD CONSTRAINT "fK_idRemiseria_Viajes" FOREIGN KEY (id_remiseria) REFERENCES public."Remiseria"(id_remiseria);
 J   ALTER TABLE ONLY public."Viajes" DROP CONSTRAINT "fK_idRemiseria_Viajes";
       public          postgres    false    216    4703    222            }           2606    16512    ChoferAuto fK_id_chofer    FK CONSTRAINT     �   ALTER TABLE ONLY public."ChoferAuto"
    ADD CONSTRAINT "fK_id_chofer" FOREIGN KEY (id_chofer) REFERENCES public."Chofer"(id_chofer);
 E   ALTER TABLE ONLY public."ChoferAuto" DROP CONSTRAINT "fK_id_chofer";
       public          postgres    false    4719    230    232            v           2606    16494    Viajes fK_patente    FK CONSTRAINT     {   ALTER TABLE ONLY public."Viajes"
    ADD CONSTRAINT "fK_patente" FOREIGN KEY (patente) REFERENCES public."Autos"(patente);
 ?   ALTER TABLE ONLY public."Viajes" DROP CONSTRAINT "fK_patente";
       public          postgres    false    4711    216    227            ~           2606    16518    ChoferAuto fK_patente_CA    FK CONSTRAINT     �   ALTER TABLE ONLY public."ChoferAuto"
    ADD CONSTRAINT "fK_patente_CA" FOREIGN KEY (patente) REFERENCES public."Autos"(patente);
 F   ALTER TABLE ONLY public."ChoferAuto" DROP CONSTRAINT "fK_patente_CA";
       public          postgres    false    230    227    4711            �           2606    16563    Recordatorios fK_patente_Record    FK CONSTRAINT     �   ALTER TABLE ONLY public."Recordatorios"
    ADD CONSTRAINT "fK_patente_Record" FOREIGN KEY (patente) REFERENCES public."Autos"(patente);
 M   ALTER TABLE ONLY public."Recordatorios" DROP CONSTRAINT "fK_patente_Record";
       public          postgres    false    4711    234    227            w           2606    16542    Viajes fK_tipoPago_Viajes    FK CONSTRAINT     �   ALTER TABLE ONLY public."Viajes"
    ADD CONSTRAINT "fK_tipoPago_Viajes" FOREIGN KEY (cod_tipo_pago) REFERENCES public."TipoPago"(cod_tipo_pago);
 G   ALTER TABLE ONLY public."Viajes" DROP CONSTRAINT "fK_tipoPago_Viajes";
       public          postgres    false    216    220    4701            x           2606    16500    Viajes fk_idPrecio    FK CONSTRAINT     �   ALTER TABLE ONLY public."Viajes"
    ADD CONSTRAINT "fk_idPrecio" FOREIGN KEY (id_precio) REFERENCES public."Precio"(id_precio);
 @   ALTER TABLE ONLY public."Viajes" DROP CONSTRAINT "fk_idPrecio";
       public          postgres    false    4699    216    218            |           2606    16530    Registro pK_Patente_Registro    FK CONSTRAINT     �   ALTER TABLE ONLY public."Registro"
    ADD CONSTRAINT "pK_Patente_Registro" FOREIGN KEY (patente) REFERENCES public."Autos"(patente);
 J   ALTER TABLE ONLY public."Registro" DROP CONSTRAINT "pK_Patente_Registro";
       public          postgres    false    227    4711    229                  x������ � �      !      x������ � �            x������ � �         z   x�3��L�SN�K�H��4�467553�00��tJ,*��W�*M�L�L�Q06�,I-.q z���`���1�!�g@jA��cQzj^I>�1�ss##�1��
����@� l�1#F��� ��(M         :   x�3��OJ-:��˘�3�4���ˈ3 �81%��˔3 1/17)�ˌ�1'5�+F��� �Il            x������ � �      #      x������ � �            x������ � �            x������ � �            x������ � �            x������ � �     