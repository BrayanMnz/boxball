# coding: utf-8
from sqlalchemy import Boolean, CHAR, Column, Date, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Event(Base):
    __tablename__ = 'events'

    game_id = Column(CHAR(12), nullable=False)
    away_team_id = Column(CHAR(3))
    inn_ct = Column(Integer)
    bat_home_id = Column(Integer)
    outs_ct = Column(Integer)
    balls_ct = Column(Integer)
    strikes_ct = Column(Integer)
    pitch_seq_tx = Column(String(40))
    away_score_ct = Column(Integer)
    home_score_ct = Column(Integer)
    bat_id = Column(CHAR(8))
    bat_hand_cd = Column(CHAR(1))
    resp_bat_id = Column(CHAR(8))
    resp_bat_hand_cd = Column(CHAR(1))
    pit_id = Column(CHAR(8))
    pit_hand_cd = Column(CHAR(1))
    resp_pit_id = Column(CHAR(8))
    resp_pit_hand_cd = Column(CHAR(1))
    pos2_fld_id = Column(CHAR(8))
    pos3_fld_id = Column(CHAR(8))
    pos4_fld_id = Column(CHAR(8))
    pos5_fld_id = Column(CHAR(8))
    pos6_fld_id = Column(CHAR(8))
    pos7_fld_id = Column(CHAR(8))
    pos8_fld_id = Column(CHAR(8))
    pos9_fld_id = Column(CHAR(8))
    base1_run_id = Column(String(8))
    base2_run_id = Column(String(8))
    base3_run_id = Column(String(8))
    event_tx = Column(String(100))
    leadoff_fl = Column(Boolean)
    ph_fl = Column(Boolean)
    bat_fld_cd = Column(Integer)
    bat_lineup_id = Column(Integer)
    event_cd = Column(Integer)
    bat_event_fl = Column(Boolean)
    ab_fl = Column(Boolean)
    h_cd = Column(Integer)
    sh_fl = Column(Boolean)
    sf_fl = Column(Boolean)
    event_outs_ct = Column(Integer)
    dp_fl = Column(Boolean)
    tp_fl = Column(Boolean)
    rbi_ct = Column(Integer)
    wp_fl = Column(Boolean)
    pb_fl = Column(Boolean)
    fld_cd = Column(Integer)
    battedball_cd = Column(CHAR(1))
    bunt_fl = Column(Boolean)
    foul_fl = Column(Boolean)
    battedball_loc_tx = Column(String(5))
    err_ct = Column(Integer)
    err1_fld_cd = Column(Integer)
    err1_cd = Column(CHAR(1))
    err2_fld_cd = Column(Integer)
    err2_cd = Column(CHAR(1))
    err3_fld_cd = Column(Integer)
    err3_cd = Column(CHAR(1))
    bat_dest_id = Column(Integer)
    run1_dest_id = Column(Integer)
    run2_dest_id = Column(Integer)
    run3_dest_id = Column(Integer)
    bat_play_tx = Column(String(8))
    run1_play_tx = Column(String(15))
    run2_play_tx = Column(String(15))
    run3_play_tx = Column(String(15))
    run1_sb_fl = Column(Boolean)
    run2_sb_fl = Column(Boolean)
    run3_sb_fl = Column(Boolean)
    run1_cs_fl = Column(Boolean)
    run2_cs_fl = Column(Boolean)
    run3_cs_fl = Column(Boolean)
    run1_pk_fl = Column(Boolean)
    run2_pk_fl = Column(Boolean)
    run3_pk_fl = Column(Boolean)
    run1_resp_pit_id = Column(String(8))
    run2_resp_pit_id = Column(String(8))
    run3_resp_pit_id = Column(String(8))
    game_new_fl = Column(Boolean)
    game_end_fl = Column(Boolean)
    pr_run1_fl = Column(Boolean)
    pr_run2_fl = Column(Boolean)
    pr_run3_fl = Column(Boolean)
    removed_for_pr_run1_id = Column(String(8))
    removed_for_pr_run2_id = Column(String(8))
    removed_for_pr_run3_id = Column(String(8))
    removed_for_ph_bat_id = Column(String(8))
    removed_for_ph_bat_fld_cd = Column(Integer)
    po1_fld_cd = Column(Integer)
    po2_fld_cd = Column(Integer)
    po3_fld_cd = Column(Integer)
    ass1_fld_cd = Column(Integer)
    ass2_fld_cd = Column(Integer)
    ass3_fld_cd = Column(Integer)
    ass4_fld_cd = Column(Integer)
    ass5_fld_cd = Column(Integer)
    event_id = Column(Integer, primary_key=True)
    home_team_id = Column(CHAR(3))
    bat_team_id = Column(CHAR(3))
    fld_team_id = Column(CHAR(3))
    bat_last_id = Column(Integer)
    inn_new_fl = Column(Boolean)
    inn_end_fl = Column(Boolean)
    start_bat_score_ct = Column(Integer)
    start_fld_score_ct = Column(Integer)
    inn_runs_ct = Column(Integer)
    game_pa_ct = Column(Integer)
    inn_pa_ct = Column(Integer)
    pa_new_fl = Column(Boolean)
    pa_trunc_fl = Column(Boolean)
    start_bases_cd = Column(Integer)
    end_bases_cd = Column(Integer)
    bat_start_fl = Column(Boolean)
    resp_bat_start_fl = Column(Boolean)
    bat_on_deck_id = Column(String(8))
    bat_in_hold_id = Column(String(8))
    pit_start_fl = Column(Boolean)
    resp_pit_start_fl = Column(Boolean)
    run1_fld_cd = Column(Integer)
    run1_lineup_cd = Column(Integer)
    run1_origin_event_id = Column(Integer)
    run2_fld_cd = Column(Integer)
    run2_lineup_cd = Column(Integer)
    run2_origin_event_id = Column(Integer)
    run3_fld_cd = Column(Integer)
    run3_lineup_cd = Column(Integer)
    run3_origin_event_id = Column(Integer)
    run1_resp_cat_id = Column(String(8))
    run2_resp_cat_id = Column(String(8))
    run3_resp_cat_id = Column(String(8))
    pa_ball_ct = Column(Integer)
    pa_called_ball_ct = Column(Integer)
    pa_intent_ball_ct = Column(Integer)
    pa_pitchout_ball_ct = Column(Integer)
    pa_hitbatter_ball_ct = Column(Integer)
    pa_other_ball_ct = Column(Integer)
    pa_strike_ct = Column(Integer)
    pa_called_strike_ct = Column(Integer)
    pa_swingmiss_strike_ct = Column(Integer)
    pa_foul_strike_ct = Column(Integer)
    pa_inplay_strike_ct = Column(Integer)
    pa_other_strike_ct = Column(Integer)
    event_runs_ct = Column(Integer)
    fld_id = Column(String(8))
    base2_force_fl = Column(Boolean)
    base3_force_fl = Column(Boolean)
    base4_force_fl = Column(Boolean)
    bat_safe_err_fl = Column(Boolean)
    bat_fate_id = Column(Integer)
    run1_fate_id = Column(Integer)
    run2_fate_id = Column(Integer)
    run3_fate_id = Column(Integer)
    fate_runs_ct = Column(Integer)
    ass6_fld_cd = Column(Integer)
    ass7_fld_cd = Column(Integer)
    ass8_fld_cd = Column(Integer)
    ass9_fld_cd = Column(Integer)
    ass10_fld_cd = Column(Integer)
    unknown_out_exc_fl = Column(Boolean)
    uncertain_play_exc_fl = Column(Boolean)


class Game(Base):
    __tablename__ = 'games'

    game_id = Column(String(12), primary_key=True)
    game_dt = Column(Integer)
    game_ct = Column(Integer)
    game_dy = Column(String(9))
    start_game_tm = Column(Integer)
    dh_fl = Column(String(1))
    daynight_park_cd = Column(String(1))
    away_team_id = Column(String(3))
    home_team_id = Column(String(3))
    park_id = Column(String(5))
    away_start_pit_id = Column(String(8))
    home_start_pit_id = Column(String(8))
    base4_ump_id = Column(String(8))
    base1_ump_id = Column(String(8))
    base2_ump_id = Column(String(8))
    base3_ump_id = Column(String(8))
    lf_ump_id = Column(String(8))
    rf_ump_id = Column(String(8))
    attend_park_ct = Column(Integer)
    scorer_record_id = Column(String(50))
    translator_record_id = Column(String(50))
    inputter_record_id = Column(String(50))
    input_record_ts = Column(String(18))
    edit_record_ts = Column(String(18))
    method_record_cd = Column(String(18))
    pitches_record_cd = Column(String(1))
    temp_park_ct = Column(Integer)
    wind_direction_park_cd = Column(Integer)
    wind_speed_park_ct = Column(Integer)
    field_park_cd = Column(Integer)
    precip_park_cd = Column(Integer)
    sky_park_cd = Column(Integer)
    minutes_game_ct = Column(Integer)
    inn_ct = Column(Integer)
    away_score_ct = Column(Integer)
    home_score_ct = Column(Integer)
    away_hits_ct = Column(Integer)
    home_hits_ct = Column(Integer)
    away_err_ct = Column(Integer)
    home_err_ct = Column(Integer)
    away_lob_ct = Column(Integer)
    home_lob_ct = Column(Integer)
    win_pit_id = Column(String(8))
    lose_pit_id = Column(String(8))
    save_pit_id = Column(String(8))
    gwrbi_bat_id = Column(String(8))
    away_lineup1_bat_id = Column(String(8))
    away_lineup1_fld_cd = Column(Integer)
    away_lineup2_bat_id = Column(String(8))
    away_lineup2_fld_cd = Column(Integer)
    away_lineup3_bat_id = Column(String(8))
    away_lineup3_fld_cd = Column(Integer)
    away_lineup4_bat_id = Column(String(8))
    away_lineup4_fld_cd = Column(Integer)
    away_lineup5_bat_id = Column(String(8))
    away_lineup5_fld_cd = Column(Integer)
    away_lineup6_bat_id = Column(String(8))
    away_lineup6_fld_cd = Column(Integer)
    away_lineup7_bat_id = Column(String(8))
    away_lineup7_fld_cd = Column(Integer)
    away_lineup8_bat_id = Column(String(8))
    away_lineup8_fld_cd = Column(Integer)
    away_lineup9_bat_id = Column(String(8))
    away_lineup9_fld_cd = Column(Integer)
    home_lineup1_bat_id = Column(String(8))
    home_lineup1_fld_cd = Column(Integer)
    home_lineup2_bat_id = Column(String(8))
    home_lineup2_fld_cd = Column(Integer)
    home_lineup3_bat_id = Column(String(8))
    home_lineup3_fld_cd = Column(Integer)
    home_lineup4_bat_id = Column(String(8))
    home_lineup4_fld_cd = Column(Integer)
    home_lineup5_bat_id = Column(String(8))
    home_lineup5_fld_cd = Column(Integer)
    home_lineup6_bat_id = Column(String(8))
    home_lineup6_fld_cd = Column(Integer)
    home_lineup7_bat_id = Column(String(8))
    home_lineup7_fld_cd = Column(Integer)
    home_lineup8_bat_id = Column(String(8))
    home_lineup8_fld_cd = Column(Integer)
    home_lineup9_bat_id = Column(String(8))
    home_lineup9_fld_cd = Column(Integer)
    away_finish_pit_id = Column(String(8))
    home_finish_pit_id = Column(String(8))
    away_team_league_id = Column(CHAR(1))
    home_team_league_id = Column(CHAR(1))
    away_team_game_ct = Column(Integer)
    home_team_game_ct = Column(Integer)
    outs_ct = Column(Integer)
    completion_tx = Column(Text)
    forfeit_tx = Column(Text)
    protest_tx = Column(Text)
    away_line_tx = Column(Text)
    home_line_tx = Column(Text)
    away_ab_ct = Column(Integer)
    away_2b_ct = Column(Integer)
    away_3b_ct = Column(Integer)
    away_hr_ct = Column(Integer)
    away_bi_ct = Column(Integer)
    away_sh_ct = Column(Integer)
    away_sf_ct = Column(Integer)
    away_hp_ct = Column(Integer)
    away_bb_ct = Column(Integer)
    away_ibb_ct = Column(Integer)
    away_so_ct = Column(Integer)
    away_sb_ct = Column(Integer)
    away_cs_ct = Column(Integer)
    away_gdp_ct = Column(Integer)
    away_xi_ct = Column(Integer)
    away_pitcher_ct = Column(Integer)
    away_er_ct = Column(Integer)
    away_ter_ct = Column(Integer)
    away_wp_ct = Column(Integer)
    away_bk_ct = Column(Integer)
    away_po_ct = Column(Integer)
    away_a_ct = Column(Integer)
    away_pb_ct = Column(Integer)
    away_dp_ct = Column(Integer)
    away_tp_ct = Column(Integer)
    home_ab_ct = Column(Integer)
    home_2b_ct = Column(Integer)
    home_3b_ct = Column(Integer)
    home_hr_ct = Column(Integer)
    home_bi_ct = Column(Integer)
    home_sh_ct = Column(Integer)
    home_sf_ct = Column(Integer)
    home_hp_ct = Column(Integer)
    home_bb_ct = Column(Integer)
    home_ibb_ct = Column(Integer)
    home_so_ct = Column(Integer)
    home_sb_ct = Column(Integer)
    home_cs_ct = Column(Integer)
    home_gdp_ct = Column(Integer)
    home_xi_ct = Column(Integer)
    home_pitcher_ct = Column(Integer)
    home_er_ct = Column(Integer)
    home_ter_ct = Column(Integer)
    home_wp_ct = Column(Integer)
    home_bk_ct = Column(Integer)
    home_po_ct = Column(Integer)
    home_a_ct = Column(Integer)
    home_pb_ct = Column(Integer)
    home_dp_ct = Column(Integer)
    home_tp_ct = Column(Integer)
    ump_home_name_tx = Column(Text)
    ump_1b_name_tx = Column(Text)
    ump_2b_name_tx = Column(Text)
    ump_3b_name_tx = Column(Text)
    ump_lf_name_tx = Column(Text)
    ump_rf_name_tx = Column(Text)
    away_manager_id = Column(String(8))
    away_manager_name_tx = Column(Text)
    home_manager_id = Column(String(8))
    home_manager_name_tx = Column(Text)
    win_pit_name_tx = Column(Text)
    lose_pit_name_tx = Column(Text)
    save_pit_name_tx = Column(Text)
    goahead_rbi_id = Column(String(8))
    goahead_rbi_name_tx = Column(Text)
    away_lineup1_bat_name_tx = Column(Text)
    away_lineup2_bat_name_tx = Column(Text)
    away_lineup3_bat_name_tx = Column(Text)
    away_lineup4_bat_name_tx = Column(Text)
    away_lineup5_bat_name_tx = Column(Text)
    away_lineup6_bat_name_tx = Column(Text)
    away_lineup7_bat_name_tx = Column(Text)
    away_lineup8_bat_name_tx = Column(Text)
    away_lineup9_bat_name_tx = Column(Text)
    home_lineup1_bat_name_tx = Column(Text)
    home_lineup2_bat_name_tx = Column(Text)
    home_lineup3_bat_name_tx = Column(Text)
    home_lineup4_bat_name_tx = Column(Text)
    home_lineup5_bat_name_tx = Column(Text)
    home_lineup6_bat_name_tx = Column(Text)
    home_lineup7_bat_name_tx = Column(Text)
    home_lineup8_bat_name_tx = Column(Text)
    home_lineup9_bat_name_tx = Column(Text)
    add_info_tx = Column(Text)
    acq_info_tx = Column(Text)


class Park(Base):
    __tablename__ = 'parks'

    park_id = Column(CHAR(5), primary_key=True)
    name = Column(Text)
    state = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date)
    league = Column(CHAR(2))
    notes = Column(Text)
    aka = Column(Text)


class Player(Base):
    __tablename__ = 'players'

    last_name = Column(Text)
    first_name = Column(Text)
    id = Column(CHAR(8), primary_key=True)
    debut = Column(Date)


class Sub(Base):
    __tablename__ = 'subs'

    game_id = Column(String(12))
    inn_ct = Column(Integer)
    bat_home_id = Column(Integer)
    sub_id = Column(String(8))
    sub_home_id = Column(Integer)
    sub_lineup_id = Column(Integer)
    sub_fld_cd = Column(Integer)
    removed_id = Column(String(8))
    removed_fld_cd = Column(Integer)
    event_id = Column(Integer, primary_key=True)


class BasesCd(Base):
    __tablename__ = 'bases_cd'

    start_bases_cd = Column(Integer, primary_key=True)
    runner_1 = Column(Integer)
    runner_2 = Column(Integer)
    runner_3 = Column(Integer)


class EventCd(Base):
    __tablename__ = 'event_cd'

    value_cd = Column(Integer, primary_key=True)
    shortname = Column(String(8))
    longname = Column(String(30))