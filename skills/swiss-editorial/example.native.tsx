import React, { useState } from 'react';
import { Pressable, ScrollView, StyleSheet, Text, TextInput, useColorScheme, View } from 'react-native';

const stories = [
  { id: '01', category: 'Design', title: 'Less noise. More meaning.', summary: 'On making room for the things that deserve our attention.', body: 'Start with what matters. Give the content room to breathe, and let the next action speak for itself.' },
  { id: '02', category: 'Culture', title: 'The city is a type specimen.', summary: 'A field guide to the letters we walk past every day.', body: 'Shopfronts, station signs, and handwritten notices tell a living story about a neighbourhood.' },
  { id: '03', category: 'Design', title: 'A grid is a starting point.', summary: 'Structure that makes space for an unexpected idea.', body: 'Align what belongs together, and break the pattern only when the content gives you a reason.' },
];
const palettes = {
  light: { bg: '#f4f1ea', ink: '#20201e', muted: '#595952', accent: '#b52e1c', onAccent: '#ffffff', focus: '#214acc' },
  dark: { bg: '#1d1e1c', ink: '#f4f1ea', muted: '#c2c0b6', accent: '#ffa48d', onAccent: '#20201e', focus: '#a4bcff' },
};

export function SwissEditorialNativeExample({ theme }: { theme?: 'light' | 'dark' }) {
  const system = useColorScheme();
  const colors = palettes[theme ?? (system === 'dark' ? 'dark' : 'light')];
  const [width, setWidth] = useState(0);
  const [query, setQuery] = useState('');
  const [category, setCategory] = useState('All');
  const [saved, setSaved] = useState<string[]>([]);
  const [focused, setFocused] = useState<string | null>(null);
  const visible = stories.filter(story => (category === 'All' || category === story.category) && `${story.title} ${story.summary}`.toLocaleLowerCase().includes(query.trim().toLocaleLowerCase()));
  const control = (key: string, label: string, selected: boolean, action: () => void, accessibleLabel = label) => (
    <Pressable key={key} accessibilityRole="button" accessibilityLabel={accessibleLabel} accessibilityState={{ selected }} onPress={action} onFocus={() => setFocused(key)} onBlur={() => setFocused(null)} style={({ pressed }) => [styles.button, { borderColor: focused === key ? colors.focus : colors.ink, backgroundColor: selected ? colors.accent : colors.bg }, (pressed || focused === key) && styles.emphasized]}>
      <Text style={{ color: selected ? colors.onAccent : colors.ink, fontWeight: '700' }}>{selected ? '✓ ' : ''}{label}</Text>
    </Pressable>
  );

  return (
    <ScrollView onLayout={event => setWidth(event.nativeEvent.layout.width)} style={{ backgroundColor: colors.bg }} contentContainerStyle={[styles.page, { padding: width >= 600 ? 32 : 16 }]} keyboardShouldPersistTaps="handled">
      <Text style={[styles.brand, { color: colors.ink }]}>FORM / FIELD</Text>
      <Text style={[styles.meta, { color: colors.muted }]}>Volume 01 / The clarity issue</Text>
      <Text accessibilityRole="header" style={[styles.title, { color: colors.ink }]}>A little less. A lot more.</Text>
      <Text style={[styles.body, { color: colors.ink }]}>Notes on thoughtful design and everyday life.</Text>
      <Text accessibilityRole="header" style={[styles.heading, { color: colors.ink }]}>The index</Text>
      <Text style={{ color: colors.ink, marginTop: 16 }}>Search the journal</Text>
      <TextInput accessibilityLabel="Search the journal" value={query} onChangeText={setQuery} onFocus={() => setFocused('search')} onBlur={() => setFocused(null)} placeholder="A title, an idea…" placeholderTextColor={colors.muted} style={[styles.input, { color: colors.ink, borderColor: focused === 'search' ? colors.focus : colors.ink }]} />
      <View style={styles.controls}>{['All', 'Design', 'Culture'].map(item => control(item, item, category === item, () => setCategory(item)))}</View>
      <Text accessibilityLiveRegion="polite" style={{ color: colors.muted }}>{visible.length} {visible.length === 1 ? 'story' : 'stories'} / {saved.length} saved</Text>
      {visible.map(story => <View key={story.id} style={[styles.article, { borderColor: colors.ink }]}>
        <Text style={{ color: colors.muted }}>{story.id} / {story.category}</Text>
        <Text accessibilityRole="header" style={[styles.heading, { color: colors.ink }]}>{story.title}</Text>
        <Text style={[styles.body, { color: colors.ink }]}>{story.summary}</Text>
        <Text style={[styles.body, { color: colors.ink }]}>{story.body}</Text>
        <View style={styles.controls}>{control(story.id, saved.includes(story.id) ? 'Saved' : 'Save', saved.includes(story.id), () => setSaved(previous => previous.includes(story.id) ? previous.filter(item => item !== story.id) : [...previous, story.id]), `${saved.includes(story.id) ? 'Saved' : 'Save'}: ${story.title}`)}</View>
      </View>)}
      {visible.length === 0 && <View><Text style={[styles.heading, { color: colors.ink }]}>No stories found</Text><View style={styles.controls}>{control('reset', 'Reset filters', false, () => { setQuery(''); setCategory('All'); })}</View></View>}
      <Text style={[styles.meta, { color: colors.muted }]}>Fictional journal. Bookmarks stay in this session.</Text>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  page: { flexGrow: 1, width: '100%', maxWidth: 880, alignSelf: 'center' },
  brand: { fontSize: 22, fontWeight: '800' },
  title: { fontSize: 44, fontWeight: '800', marginTop: 24 },
  heading: { fontSize: 26, fontWeight: '700', marginTop: 24 },
  meta: { fontSize: 14, marginTop: 16 },
  body: { fontSize: 18, marginTop: 16 },
  controls: { flexDirection: 'row', flexWrap: 'wrap', gap: 8, marginVertical: 16 },
  button: { minHeight: 48, minWidth: 48, padding: 12, justifyContent: 'center', borderWidth: 1 },
  emphasized: { borderWidth: 3, padding: 10 },
  input: { minHeight: 48, borderWidth: 2, padding: 12, fontSize: 18, marginTop: 8 },
  article: { borderTopWidth: 1, paddingTop: 24, marginTop: 24 },
});

// Verification: type-checked against React Native; device accessibility remains a host integration check.
// Fallback: no blur, shadow, animation, or custom font; retain text, selected state and native controls.
